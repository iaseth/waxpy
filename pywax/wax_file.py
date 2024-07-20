from .wax_header import WaxHeader
from .utils import bytes_to_candle



class WaxFile:
	def __init__(self, filepath):
		with open(filepath, 'rb') as f:
			self.header = WaxHeader(f)
			self.candles = []

			for row_index in range(self.header.row_count):
				candle_bytes = f.read(self.header.row_length)
				if not candle_bytes: break
				candle = bytes_to_candle(candle_bytes)
				self.candles.append(candle)


	def print_candles(self):
		for idx, candle in enumerate(self.candles):
			print(f"{idx+1}. {candle}")


