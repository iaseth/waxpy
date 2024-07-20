from .utils import bytes_to_candle



class WaxFile:
	def __init__(self, filepath):
		with open(filepath, 'rb') as f:
			header_bytes = f.read(16)

			self.candles = []
			while True:
				candle_bytes = f.read(24)
				if candle_bytes:
					candle = bytes_to_candle(candle_bytes)
					self.candles.append(candle)
				else:
					break

	def print_candles(self):
		for idx, candle in enumerate(self.candles):
			print(f"{idx+1}. {candle}")


