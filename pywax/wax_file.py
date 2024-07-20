from .wax_candle import WaxCandle
from .wax_header import WaxHeader



class WaxFile:
	def __init__(self, filepath):
		with open(filepath, 'rb') as f:
			self.header = WaxHeader(f)
			self.candles = []

			for row_index in range(self.header.row_count):
				candle_bytes = f.read(self.header.row_length)
				if not candle_bytes: break
				candle = WaxCandle(candle_bytes, row_index)
				self.candles.append(candle)


	def print_candles(self):
		for candle in self.candles:
			print(candle)


