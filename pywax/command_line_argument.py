import os

from .get_candles_from_file import get_candles_from_file
from .wax_header import WaxHeader



class CommandLineArgument:
	def __init__(self, arg):
		self.arg = arg
		self.next = None
		self.prev = None

	def is_flag(self):
		return True if self.arg[0] == '-' else False

	def is_not_flag(self):
		return True if self.arg[0] != '-' else False

	def is_single_flag(self):
		return True if self.arg[0] == '-' and self.arg[1] != '-' else False

	def is_double_flag(self):
		return True if self.arg[0] == '-' and self.arg[1] == '-' and self.arg[2] != '-' else False

	def is_input_filepath(self):
		if self.is_flag(): return False
		if self.prev and self.prev.arg == '-o': return False
		return True

	def is_output_filepath(self):
		if self.is_not_flag() and self.prev and self.prev.arg == '-o':
			return True
		return False

	def isfile(self):
		return os.path.isfile(self.arg)

	def isdir(self):
		return os.path.isdir(self.arg)

	def get_candles_from_file(self):
		candles_in_file = get_candles_from_file(self.arg)
		return candles_in_file

	def get_candles_from_directory(self):
		if not self.isdir(): return []
		filenames = os.listdir(self.arg)
		filenames.sort()
		filepaths = [os.path.join(self.arg, f) for f in filenames]

		candles = []
		for filepath in filepaths:
			candles_in_file = get_candles_from_file(filepath)
			candles.extend(candles_in_file)

		candles.sort()
		return candles

	def get_header(self):
		header = None
		if self.isfile():
			with open(self.arg, 'rb') as f:
				header = WaxHeader(f)
		return header

	def __repr__(self):
		return f"'{self.arg}'"

