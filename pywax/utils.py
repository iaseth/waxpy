


HEADER_LENGTH = 16


def bint(integer, width=4):
	integer_bytes = (integer).to_bytes(width, 'big')
	return integer_bytes


def intb(integer_bytes):
	integer = int.from_bytes(integer_bytes, 'big')
	return integer


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


