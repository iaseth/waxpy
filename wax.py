#!/usr/bin/python3
import json
import os

from pywax import candle_to_bytes, get_header_bytes, get_args



def candles_to_csv(candles, output_filepath):
	pass


def candles_to_json(candles, output_filepath):
	pass


def candles_to_wax(candles, output_filepath):
	n_candles = len(candles)
	header_lines_count = 0
	column_count = 6
	row_length = 24
	row_count = len(candles)

	out = open(output_filepath, 'wb') if output_filepath else None

	header = get_header_bytes(header_lines_count, column_count, row_length, row_count)
	if out:
		out.write(header)

	for idx, candle in enumerate(candles):
		candle_bytes = candle_to_bytes(candle)
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


def print_candles(candles):
	print(f"Found {len(candles)} candles.")
	for idx, candle in enumerate(candles):
		print(f"{idx+1}. {candle}")
	print(f"Found {len(candles)} candles.")



def main():
	args = get_args()

	if len(args) == 0:
		return

	input_filepaths = [arg for arg in args if arg.is_input_filepath()]
	output_filepaths = [arg for arg in args if arg.is_output_filepath()]
	single_flags = [arg for arg in args if arg.is_single_flag()]
	double_flags = [arg for arg in args if arg.is_double_flag()]

	if len(input_filepaths) == 0:
		print(f"No input file path supplied!")
		return

	if len(output_filepaths) > 1:
		print(f"Too many output file paths supplied!")
		return

	input_filepath = input_filepaths[0].arg
	output_filepath = output_filepaths[0].arg if len(output_filepaths) == 1 else None

	candles = []
	for input_filepath in input_filepaths:
		if input_filepath.isfile():
			candles_in_file = input_filepath.get_candles_from_file()
			candles.extend(candles_in_file)
		else:
			print(f"File NOT found: {input_filepath.arg}")
			return

	if not output_filepath:
		print_candles(candles)
	elif output_filepath.endswith('.csv'):
		candles_to_wax(candles, output_filepath)
	elif output_filepath.endswith('.json'):
		candles_to_json(candles, output_filepath)
	elif output_filepath.endswith('.wax'):
		candles_to_wax(candles, output_filepath)
	else:
		print(f"Output format not supported: {output_filepath}")



if __name__ == '__main__':
	main()
