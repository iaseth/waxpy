from .common import WAX_VERSION_NUMBER
from .utils import bint, intb
from .utils import zeroes, count_non_zeroes



class EncodingScheme:
	def __init__(self, code, codeName, widths, multipliers):
		self.code = code
		self.codeName = codeName
		self.count = count_non_zeroes(widths)
		self.widths = widths
		self.multipliers = multipliers
		self.width = sum(widths)


	def get_encoder(self):
		count = self.count
		widths = self.widths
		multipliers = self.multipliers

		def encoder(candle):
			components = candle.components(count)
			if len(components) != count: return None
			components = [int(val * multipliers[idx]) for idx, val in enumerate(components)]
			byte_candle = [bint(val, widths[idx]) for idx, val in enumerate(components)]
			candle_bytes = b''.join(byte_candle)
			return candle_bytes

		return encoder


	def get_decoder(self):
		count = self.count
		widths = self.widths
		multipliers = self.multipliers

		def decoder(candle_bytes):
			if len(candle_bytes) != self.width: return None
			components = zeroes(count)

			start = 0
			for x in range(count):
				end = start + widths[x]
				num = intb(candle_bytes[start:end])
				components[x] = num if multipliers[x] == 1 else num / multipliers[x]
				start = end

			return components

		return decoder


	def get_header_bytes(self, header_lines_count, row_count):
		parts = [
			bint(WAX_VERSION_NUMBER, 2),
			bint(self.code, 2),

			bint(header_lines_count, 1),
			bint(self.count, 1),
			bint(self.width, 2),

			bint(row_count, 4),
			bint(0, 4),
		]
		header_bytes = b''.join(parts)
		return header_bytes


	def get_codename_bytes(self):
		byte_candle = []
		for i in range(14):
			ch = self.codeName[i] if len(self.codeName) > i else ' '
			b = ch.encode()
			byte_candle.append(b)
		return byte_candle

	def get_widths_bytes(self):
		byte_candle = []
		for i in range(16):
			x = self.widths[i] if len(self.widths) > i else 0
			b = bint(x, 1)
			byte_candle.append(b)
		return byte_candle

	def get_multipliers_bytes(self):
		byte_candle = []
		for i in range(16):
			x = self.multipliers[i] if len(self.multipliers) > i else 1
			b = bint(x, 1)
			byte_candle.append(b)
		return byte_candle

	def to_bytes(self):
		code_bytes = bint(self.code, 2)
		byte_candle = [code_bytes]
		byte_candle.extend(self.get_codename_bytes())
		byte_candle.extend(self.get_widths_bytes())
		byte_candle.extend(self.get_multipliers_bytes())
		candle_bytes = b''.join(byte_candle)
		return candle_bytes


	def __repr__(self):
		codeName = f"'{self.codeName}'"
		widths_string = [str(x) for x in self.widths]
		widths_string = "+".join(widths_string)
		return f"Encoding {codeName:14} {self.code}b [{widths_string}]"


