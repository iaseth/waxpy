import datetime

from .utils import bytes_to_candle



class WaxCandle:
	def __init__(self, candle_bytes, idx):
		self.idx = idx
		parts = bytes_to_candle(candle_bytes)
		self.timestamp = parts[0]
		self.open = parts[1]
		self.high = parts[2]
		self.low = parts[3]
		self.close = parts[4]
		self.volume = parts[5]
		self.open_interest = 0


	def datetime_string(self):
		date = datetime.datetime.fromtimestamp(self.timestamp)
		return str(date)


	def __str__(self):
		datetime_string = self.datetime_string()
		date, time = datetime_string.split(' ')
		return f"| {self.idx+1:4} | {date} | {time} | {self.open:8.2f} | {self.high:8.2f} | {self.low:8.2f} | {self.close:8.2f} | {self.volume/1000_000:5.2f} M |"


