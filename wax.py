#!/usr/bin/python3
import json
import os

from pywax import get_args, get_encoding_from_code, WAX_VERSION, ENCODINGS



def get_candles_from_input_filepaths(input_filepaths):
	candles = []
	for input_filepath in input_filepaths:
		if input_filepath.isfile():
			candles_in_file = input_filepath.get_candles_from_file()
			candles.extend(candles_in_file)
		else:
			print(f"File NOT found: {input_filepath.arg}")

	return candles


def csv_command(input_filepaths, output_filepath):
	if len(input_filepaths) == 0:
		print(f"No input file path supplied!")
		return

	if not output_filepath:
		print(f"No output file supplied!")
		return

	candles = get_candles_from_input_filepaths(input_filepaths)


def json_command(input_filepaths, output_filepath):
	if len(input_filepaths) == 0:
		print(f"No input file path supplied!")
		return

	if not output_filepath:
		print(f"No output file supplied!")
		return

	candles = get_candles_from_input_filepaths(input_filepaths)


def wax_command(input_filepaths, output_filepath):
	if len(input_filepaths) == 0:
		print(f"No input file path supplied!")
		return

	if not output_filepath:
		print(f"No output file supplied!")
		return

	candles = get_candles_from_input_filepaths(input_filepaths)
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

	candles = get_candles_from_input_filepaths(input_filepaths)

	print(f"Found {len(candles)} candles.")
	for idx, candle in enumerate(candles):
		print(f"{idx+1}. {candle}")
	print(f"Found {len(candles)} candles.")


def help_command():
	print(f"List of available commands:")
	print(f"\tCSV      - Compile one or more files into CSV file.")
	print(f"\tJSON     - Compile one or more files into JSON file.")
	print(f"\tWAX      - Compile one or more files into WAX file.")
	print(f"\tHELP     - Display help information.")
	print(f"\tVERSION  - Display version information.")


def version_command():
	print(f"This is Wax Version {WAX_VERSION} with {len(ENCODINGS)} encodings.")


def unknown_command(command: str):
	print(f"Unknown command: '{command}'")



def main():
	command, args = get_args()
	command = command.upper()

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
		case 'CSV' | 'C':
			csv_command(input_filepaths, output_filepath)
		case 'JSON' | 'J':
			json_command(input_filepaths, output_filepath)
		case 'WAX' | 'W':
			wax_command(input_filepaths, output_filepath)
		case 'PRINT' | 'P':
			print_command(input_filepaths)

		case 'HELP' | 'H':
			help_command()
		case 'VERSION' | 'V':
			version_command()
		case _:
			unknown_command(command)



if __name__ == '__main__':
	main()
