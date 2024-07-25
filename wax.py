#!/usr/bin/python3
import json
import os

from pywax import WaxFile, candle_to_bytes, get_header_bytes, get_args



def unwax(input_filepath, output_filepath):
	wax = WaxFile(input_filepath)
	wax.print_candles()


def wax(input_filepath, output_filepath):
	with open(input_filepath) as f:
		jo = json.load(f)

	candles = jo['candles']
	# if not output_filepath: return

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
		print(f"Saved: {output_filepath}")



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
	output_filepath = output_filepaths[0].arg if len(output_filepaths) > 0 else None

	candles = []
	for input_filepath in input_filepaths:
		if input_filepath.isfile():
			candles_in_file = input_filepath.get_candles_from_file()
			candles.extend(candles_in_file)
		else:
			print(f"File NOT found: {input_filepath.arg}")
			return

	print(f"Found {len(candles)} candles.")
	for idx, candle in enumerate(candles):
		print(f"{idx+1}. {candle}")
	print(f"Found {len(candles)} candles.")
	return

	if input_filepath.endswith('.wax'):
		unwax(input_filepath, output_filepath)
	elif input_filepath.endswith('.json'):
		wax(input_filepath, output_filepath)


if __name__ == '__main__':
	main()
