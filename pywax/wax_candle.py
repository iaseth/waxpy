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

	def components(self, n=5):
		if n == 5:
			return [self.timestamp, self.open, self.high, self.low, self.close]
		else:
			return [self.timestamp, self.open, self.high, self.low, self.close, self.volume]


	def date(self):
		date = datetime.datetime.fromtimestamp(self.timestamp)
		return date

	def date_string(self):
		return str(self.date())[:10]

	def datetime_string(self):
		return str(self.date())


	def overlaps(self, level, strict=False, leeway=0):
		high = max(self.open, self.close) if strict else self.high
		low = min(self.open, self.close) if strict else self.low

		if leeway:
			high += leeway
			low -= leeway

		if high >= level and low <= level:
			return True
		else:
			return False


	def __lt__(self, other):
		return True if self.timestamp < other.timestamp else False


	def __str__(self):
		datetime_string = self.datetime_string()
		date, time = datetime_string.split(' ')
		candle_string = f"| {date} | {time} |"
		candle_string += f" {self.open:8.2f} | {self.high:8.2f} | {self.low:8.2f} | {self.close:8.2f} |"
		candle_string += f" {self.volume/1000_000:5.2f} M |"
		candle_string += f" {self.open_interest/1000_000:5.2f} M |"
		return candle_string


