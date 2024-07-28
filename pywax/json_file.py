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


def parts_from_data_dict(data, idx):
	return [
		data['t'][idx],
		data['o'][idx],
		data['h'][idx],
		data['l'][idx],
		data['c'][idx],
		data['v'][idx]
	]


def json_to_candles(jo):
	candles = []
	if 'candles' in jo and type(jo['candles']) is list and len(jo['candles']) > 0:
		data = jo['candles']
		first_data_point = data[0]
		if type(first_data_point) is list:
			candles = [WaxCandle(parts) for parts in data]
		elif type(first_data_point) is dict:
			candles = [WaxCandle(parts_from_candle_dict(cj)) for cj in data]
	elif 'data' in jo and type(jo['data']) is dict:
		data = jo['data']
		if 't' in data and 'o' in data and 'h' in data and 'l' in data and 'c' in data and 'v' in data:
			if type(data['t']) is list:
				candles = [WaxCandle(parts_from_data_dict(data, idx)) for idx, _ in enumerate(data['t'])]

	candles.sort()
	return candles



class JsonFile:
	def __init__(self, filepath):
		self.filepath = filepath
		self.candles = []
		if os.path.isfile(self.filepath):
			with open(self.filepath) as f:
				jo = json.load(f)
			self.candles = json_to_candles(jo)


