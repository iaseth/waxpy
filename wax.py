#!/usr/bin/python3
import json
import sys



HEADER_LENGTH = 16


def bint(integer, width=4):
	integer_bytes = (integer).to_bytes(width, 'big')
	return integer_bytes


def get_header_bytes(header_lines_count, column_count, row_length, row_count):
	parts = [
		bint(0, 2),
		bint(0, 2),

		bint(header_lines_count, 1),
		bint(column_count, 1),
		bint(row_length, 2),

		bint(row_count, 4),
		bint(0, 4),
	]
	header_bytes = b''.join(parts)
	return header_bytes


def candle_to_bytes(candle):
	t = candle[0]
	v = candle[5] if candle[5] else 0
	ohlc = candle[1:5]
	ohlc = [int(x*100) for x in ohlc]
	new_candle = [t, *ohlc, v]
	byte_candle = [bint(x, 4) for x in new_candle]
	candle_bytes = b''.join(byte_candle)
	return candle_bytes


def bytes_to_candle(candle_bytes):
	candle = [0, 0, 0, 0, 0, 0]
	for x in range(6):
		start = x * 4
		end = start + 4
		candle[x] = int.from_bytes(candle_bytes[start:end], 'big')

	for x in range(1, 5):
		candle[x] = candle[x] / 100

	return candle


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
