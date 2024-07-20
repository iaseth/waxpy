from .utils import bytes_to_candle



class WaxCandle:
	def __init__(self, candle_bytes):
		parts = bytes_to_candle(candle_bytes)
		self.timestamp = parts[0]
		self.open = parts[1]
		self.high = parts[2]
		self.low = parts[3]
		self.close = parts[4]
		self.volume = parts[5]
		self.open_interest = 0


	def __str__(self):
		return f"| {self.timestamp} | {self.open:8.2f} | {self.high:8.2f} | {self.low:8.2f} | {self.close:8.2f} | {self.volume/1000:6.0f}k |"


