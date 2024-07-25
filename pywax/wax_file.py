from .encodings import get_encoding_from_code
from .wax_candle import WaxCandle
from .wax_header import WaxHeader



class WaxFile:
	def __init__(self, filepath):
		with open(filepath, 'rb') as f:
			self.header = WaxHeader(f)
			self.encoding = get_encoding_from_code(self.header.encoding)
			self.decoder = self.encoding.get_decoder()
			self.candles = []

			for row_index in range(self.header.row_count):
				candle_bytes = f.read(self.header.row_length)
				if not candle_bytes: break
				candle = WaxCandle(candle_bytes, row_index, self.decoder)
				self.candles.append(candle)


	def print_candles(self):
		for candle in self.candles:
			print(candle)


