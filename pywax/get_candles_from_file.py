import os

from .json_file import JsonFile
from .wax_file import WaxFile



def get_candles_from_file(filepath):
	if not os.path.isfile(filepath):
		return []

	if filepath.endswith('.wax'):
		wax = WaxFile(filepath)
		return wax.candles
	elif filepath.endswith('.json'):
		jo = JsonFile(filepath)
		return jo.candles
	else:
		return []

