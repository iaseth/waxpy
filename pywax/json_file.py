import json
import os

from .wax_candle import WaxCandle



def json_to_candles(jo):
	candles = []
	if 'candles' in jo:
		candles_data = jo['candles']
		candles = [WaxCandle(parts, idx) for idx, parts in enumerate(candles_data)]
	elif 'data' in jo:
		pass

	return candles



class JsonFile:
	def __init__(self, filepath):
		self.filepath = filepath
		if os.path.isfile(self.filepath):
			with open(self.filepath) as f:
				jo = json.load(f)
				self.candles = json_to_candles(jo)
		else:
			self.candles = []


