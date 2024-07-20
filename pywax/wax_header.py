from .utils import intb



class WaxHeader:
	def __init__(self, file_reader):
		self.first_line = file_reader.read(16)
		self.lines = []

		self.version = intb(self.first_line[0:2])
		self.format = intb(self.first_line[2:4])
		self.header_lines_count = intb(self.first_line[4:5])
		self.column_count = intb(self.first_line[5:6])
		self.row_length = intb(self.first_line[6:8])
		self.row_count = intb(self.first_line[8:12])
		self.default_value = intb(self.first_line[12:16])


	def print(self):
		print(f"\tVersion: {self.version}")
		print(f"\tFormat: {self.format}")
		print(f"\tHeaders: {self.header_lines_count}")
		print(f"\tColumns: {self.column_count}")
		print(f"\tLength: {self.row_length}")
		print(f"\tRows: {self.row_count}")
		print(f"\tDefault: {self.default_value}")


