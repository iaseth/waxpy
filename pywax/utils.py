


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


