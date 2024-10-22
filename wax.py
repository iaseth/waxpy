#!/usr/bin/python3
import datetime
import json
import os

from pywax import get_args, get_encoding_from_code, WaxCandleGroup
from pywax import WAX_VERSION, ENCODINGS



def get_candles_from_input_paths(input_paths):
	candles = []
	for input_path in input_paths:
		if input_path.isfile():
			candles_in_file = input_path.get_candles_from_file()
			candles.extend(candles_in_file)
		elif input_path.isdir():
			candles_in_directory = input_path.get_candles_from_directory()
			candles.extend(candles_in_directory)
		else:
			print(f"File NOT found: {input_path.arg}")

	return candles


def analyze_command(input_filepaths, output_filepath):
	if len(input_filepaths) == 0:
		print(f"No input file path supplied!")
		return

	candles = get_candles_from_input_paths(input_filepaths)

	start_date = datetime.datetime(2024, 1, 1)
	start_timestamp = start_date.timestamp()
	candles = [c for c in candles if c.timestamp > start_timestamp]

	date_strings = [c.date_string() for c in candles]
	date_strings = sorted(list(set(date_strings)))

	one_day = datetime.timedelta(days=1)
	for idx, date_string in enumerate(date_strings):
		# print(f"{idx+1:3} | {len(date_strings)} -- {date_string} -- ", end='')
		print(f"{date_string} -- ", end='')
		parts = [int(p) for p in date_string.split('-')]

		start_date = datetime.datetime(*parts)
		end_date = start_date + one_day
		start_timestamp = start_date.timestamp()
		end_timestamp = end_date.timestamp()

		day_candles = [c for c in candles if c.timestamp > start_timestamp and c.timestamp < end_timestamp]
		day = WaxCandleGroup(day_candles, step=50)
		print(f"{day.open:5.0f} {day.high:5.0f} {day.low:5.0f} {day.close:5.0f} -- ", end='')
		levels = day.get_important_levels(min_overlap_count=20, strict=True, leeway=10)
		print(levels[:8])


def csv_command(input_filepaths, output_filepath):
	if len(input_filepaths) == 0:
		print(f"No input file path supplied!")
		return

	if not output_filepath:
		print(f"No output file supplied!")
		return

	candles = get_candles_from_input_paths(input_filepaths)


def json_command(input_filepaths, output_filepath):
	if len(input_filepaths) == 0:
		print(f"No input file path supplied!")
		return

	if not output_filepath:
		print(f"No output file supplied!")
		return

	candles = get_candles_from_input_paths(input_filepaths)


def wax_command(input_filepaths, output_filepath):
	if len(input_filepaths) == 0:
		print(f"No input file path supplied!")
		return

	if not output_filepath:
		print(f"No output file supplied!")
		return

	candles = get_candles_from_input_paths(input_filepaths)
	encoding = get_encoding_from_code(32)

	n_candles = len(candles)
	header_lines_count = 0
	row_count = len(candles)

	out = open(output_filepath, 'wb') if output_filepath else None

	header = encoding.get_header_bytes(header_lines_count, row_count)
	if out:
		out.write(header)

	encoder = encoding.get_encoder()

	for idx, candle in enumerate(candles):
		candle_bytes = encoder(candle)
		if out:
			out.write(candle_bytes)
		else:
			print(f"{idx+1}. {candle}")
		# break

	if out:
		out.close()
		size = os.path.getsize(output_filepath)
		kb = size / 1000
		bytes_per_candle = size / n_candles
		print(f"Saved: {output_filepath} ({n_candles} candles) [{kb:.1f} kB] ({bytes_per_candle:.1f} bpc)")


def print_command(input_filepaths):
	if len(input_filepaths) == 0:
		print(f"No input file path supplied!")
		return

	candles = get_candles_from_input_paths(input_filepaths)

	print(f"Found {len(candles)} candles.")
	for idx, candle in enumerate(candles):
		print(f"{idx+1}. {candle}")
	print(f"Found {len(candles)} candles.")


def raw_command(input_filepaths):
	if len(input_filepaths) == 0:
		print(f"No input file path supplied!")
		return

	candles = get_candles_from_input_paths(input_filepaths)

	print(f"Found {len(candles)} candles.")
	for idx, candle in enumerate(candles):
		print(f"{idx+1}. {candle.components(6)}")
	print(f"Found {len(candles)} candles.")


def encodings_command():
	print(f"Wax Version {WAX_VERSION} comes with {len(ENCODINGS)} encodings:")
	for idx, encoding in enumerate(ENCODINGS):
		print(f"\t{idx+1:3}. {encoding}")


def export_command(first_arg, output_filepath):
	if not output_filepath:
		output_filepath = "ENCODINGS"

	with open(output_filepath, 'wb') as f:
		for encoding in ENCODINGS:
			f.write(encoding.to_bytes())

	print(f"Saved: {output_filepath} ({len(ENCODINGS)} encodings) [{first_arg}]")


def export_json_command(output_filepath):
	if not output_filepath:
		output_filepath = "encodings.json"

	encodings = []
	for encoding in ENCODINGS:
		encodings.append(encoding.to_json())

	jo = {}
	jo['encodings'] = encodings
	output_filepath = 'encodings.json'
	with open(output_filepath, 'w') as f:
		json.dump(jo, f, sort_keys=True, indent='\t')
	print(f"Saved: {output_filepath} ({len(ENCODINGS)} encodings)")


def header_command(input_filepaths):
	if len(input_filepaths) == 0:
		print(f"No input file path supplied!")
		return

	for input_filepath in input_filepaths:
		if input_filepath.isfile():
			print(f"File: {input_filepath.arg}")
			header = input_filepath.get_header()
			header.print()
		else:
			print(f"Not Found: {input_filepath.arg}")


def help_command():
	print(f"List of available commands:")
	print(f"\tCSV         - Compile one or more files into CSV file.")
	print(f"\tJSON        - Compile one or more files into JSON file.")
	print(f"\tWAX         - Compile one or more files into WAX file.")
	print(f"\tPRINT       - Print formatted candles from one or more files to the console.")
	print(f"\tRAW         - Print raw candle data from one or more files to the console.")

	print(f"\tENCODINGS   - List all supported encodings.")
	print(f"\tEXPORT      - Export all supported encodings to a file.")
	print(f"\tHELP        - Display help information.")
	print(f"\tVERSION     - Display version information.")
	print(f"\tXPERIMENT   - For testing purposes.")


def version_command():
	print(f"This is Wax Version {WAX_VERSION} with {len(ENCODINGS)} encodings.")


def xperiment_command():
	encodings = []
	for encoding in ENCODINGS:
		encodings.append(encoding.to_json())

	jo = {}
	jo['encodings'] = encodings
	output_filepath = 'encodings.json'
	with open(output_filepath, 'w') as f:
		json.dump(jo, f, sort_keys=True, indent='\t')
	print(f"Saved: {output_filepath}")


def unknown_command(command: str):
	print(f"Unknown command: '{command}'")



def main():
	command, args = get_args()
	command = command.upper()
	first_arg = args[0].arg if len(args) > 0 else None

	if not command:
		print(f"No command supplied!")
		print(f"\t$ wax.py command args")
		return

	input_filepaths = [arg for arg in args if arg.is_input_filepath()]
	output_filepaths = [arg for arg in args if arg.is_output_filepath()]

	if len(output_filepaths) > 1:
		print(f"Too many output file paths supplied!")
		return

	output_filepath = output_filepaths[0].arg if len(output_filepaths) == 1 else None
	single_flags = [arg for arg in args if arg.is_single_flag()]
	double_flags = [arg for arg in args if arg.is_double_flag()]

	match command:
		case 'ANALYZE' | 'A':
			analyze_command(input_filepaths, output_filepath)
		case 'CSV' | 'C':
			csv_command(input_filepaths, output_filepath)
		case 'JSON' | 'J':
			json_command(input_filepaths, output_filepath)
		case 'WAX' | 'W':
			wax_command(input_filepaths, output_filepath)
		case 'PRINT' | 'P':
			print_command(input_filepaths)
		case 'RAW' | 'R':
			raw_command(input_filepaths)

		case 'ENCODINGS' | 'E':
			encodings_command()
		case 'EXPORT':
			export_command(first_arg, output_filepath)
		case 'EXPORT-JSON':
			export_json_command(output_filepath)
		case 'HEADER' | 'HD':
			header_command(input_filepaths)
		case 'HELP' | 'H':
			help_command()
		case 'VERSION' | 'V':
			version_command()
		case 'XPERIMENT' | 'X':
			xperiment_command()
		case _:
			unknown_command(command)



if __name__ == '__main__':
	main()
