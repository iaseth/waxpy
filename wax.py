#!/usr/bin/python3
import json
import sys

from pywax import bytes_to_candle, candle_to_bytes, get_header_bytes



def unwax(input_filepath, output_filepath):
	with open(input_filepath, 'rb') as f:
		header_bytes = f.read(16)

		idx = 0
		while True:
			candle_bytes = f.read(24)
			if candle_bytes:
				candle = bytes_to_candle(candle_bytes)
				print(f"{idx+1}. {candle}")
				idx += 1
			else:
				break


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
	args = sys.argv[1:]
	if len(args) == 0:
		return

	input_filepath = args[0]
	output_filepath = args[1] if len(args) > 1 else None
	if input_filepath.endswith('.wax'):
		unwax(input_filepath, output_filepath)
	elif input_filepath.endswith('.json'):
		wax(input_filepath, output_filepath)


if __name__ == '__main__':
	main()
