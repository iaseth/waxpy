from .utils import bint, intb, zeroes, get_header_bytes



class EncodingScheme:
	def __init__(self, code, codeName, widths, multipliers):
		self.code = code
		self.codeName = codeName
		self.count = len(widths)
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
		return get_header_bytes(header_lines_count, self.count, self.width, row_count)


	def __repr__(self):
		return f"Encoding '{self.codeName}' ({self.code}) {self.widths}"


