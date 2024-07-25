import datetime
import json
import os

from .wax_candle import WaxCandle



def iso_to_unix(iso: str):
	d = datetime.datetime.fromisoformat(iso)
	return int(d.timestamp())

def parts_from_candle_dict(candle):
	return [
		iso_to_unix(candle['date']),
		candle['open'], candle['high'], candle['low'], candle['close'],
		candle['volume'],
		candle['oi'] if 'oi' in candle else 0
	]


def json_to_candles(jo):
	candles = []
	if 'candles' in jo and type(jo['candles']) is list and len(jo['candles']) > 0:
		candles_data = jo['candles']
		first_data_point = candles_data[0]
		if type(first_data_point) is list:
			candles = [WaxCandle(parts, idx) for idx, parts in enumerate(candles_data)]
		elif type(first_data_point) is dict:
			candles = [WaxCandle(parts_from_candle_dict(cj), idx) for idx, cj in enumerate(candles_data)]
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


