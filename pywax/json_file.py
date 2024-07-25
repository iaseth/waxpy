


def json_to_candles(jo):
	candles = []
	if 'candles' in jo:
		candles_data = jo['candles']
	elif 'data' in jo:
		pass

	return candles



class JsonFile:
	def __init__(self, filepath):
		self.filepath = filepath
		self.candles = []


