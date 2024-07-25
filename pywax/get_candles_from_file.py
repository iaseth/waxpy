import os

from .csv_file import CsvFile
from .json_file import JsonFile
from .wax_file import WaxFile



def get_candles_from_csv_file(filepath):
	csv = CsvFile(filepath)
	return csv.candles


def get_candles_from_json_file(filepath):
	jo = JsonFile(filepath)
	return jo.candles


def get_candles_from_wax_file(filepath):
	wax = WaxFile(filepath)
	return wax.candles


def get_candles_from_file(filepath):
	if not os.path.isfile(filepath):
		return []

	if filepath.endswith('.csv'):
		return get_candles_from_csv_file(filepath)
	elif filepath.endswith('.json'):
		return get_candles_from_json_file(filepath)
	elif filepath.endswith('.wax'):
		return get_candles_from_wax_file(filepath)
	else:
		return []

