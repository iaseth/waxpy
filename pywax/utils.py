


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


