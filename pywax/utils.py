


HEADER_LENGTH = 16


def bint(integer, width=4):
	integer_bytes = (integer).to_bytes(width, 'big')
	return integer_bytes


def intb(integer_bytes):
	integer = int.from_bytes(integer_bytes, 'big')
	return integer


def zeroes(n: int):
	match(n):
		case 0: return []
		case 1: return [0]
		case 2: return [0, 0]
		case 3: return [0, 0, 0]
		case 4: return [0, 0, 0, 0]
		case 5: return [0, 0, 0, 0, 0]
		case 6: return [0, 0, 0, 0, 0, 0]
		case 7: return [0, 0, 0, 0, 0, 0, 0]
		case 8: return [0, 0, 0, 0, 0, 0, 0, 0]
		case _: return []


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


