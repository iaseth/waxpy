


class WaxCandleGroup:
	def __init__(self, candles, step=25):
		self.candles = candles
		self.open = self.candles[0].open
		self.close = self.candles[-1].open

		highs = [c.high for c in candles]
		lows = [c.low for c in candles]
		self.high = max(highs)
		self.low = min(lows)
		self.levels = []
		for level in range(int(self.low), int(self.high), 1):
			if level % step == 0:
				self.levels.append(level)

	def get_important_levels(self, min_overlap_count=15, strict=False, leeway=0):
		important_levels = []
		for level in self.levels:
			overlap_count = self.get_overlap_count(level, strict=strict, leeway=leeway)
			if overlap_count >= min_overlap_count:
				important_levels.append([level, overlap_count])

		important_levels.sort(key=lambda x:x[1])
		important_levels.reverse()
		return important_levels

	def get_overlap_count(self, level, strict=False, leeway=0):
		count = 0
		for candle in self.candles:
			if candle.overlaps(level, strict=strict, leeway=leeway):
				count += 1
		return count

