import datetime



class WaxCandle:
	def __init__(self, parts):
		self.timestamp = parts[0]
		self.open = parts[1]
		self.high = parts[2]
		self.low = parts[3]
		self.close = parts[4]
		self.volume = parts[5] if len(parts) > 5 and parts[5] else 0
		self.open_interest = parts[6] if len(parts) > 6 and parts[6] else 0


	@property
	def ohlc(self):
		return [self.open, self.high, self.low, self.close]

	def components(self, n):
		if n == 5:
			return [self.timestamp, self.open, self.high, self.low, self.close]
		else:
			return [self.timestamp, self.open, self.high, self.low, self.close, self.volume]


	def datetime_string(self):
		date = datetime.datetime.fromtimestamp(self.timestamp)
		return str(date)


	def __str__(self):
		datetime_string = self.datetime_string()
		date, time = datetime_string.split(' ')
		candle_string = f"| {date} | {time} |"
		candle_string += f" {self.open:8.2f} | {self.high:8.2f} | {self.low:8.2f} | {self.close:8.2f} |"
		candle_string += f" {self.volume/1000_000:5.2f} M |"
		candle_string += f" {self.open_interest/1000_000:5.2f} M |"
		return candle_string


