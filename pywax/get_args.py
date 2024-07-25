import sys



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

	def __repr__(self):
		return f"'{self.arg}'"



def get_args():
	args = sys.argv[1:]
	arg_objects = []
	last_object = None
	for arg in args:
		arg_object = CommandLineArgument(arg)
		if last_object:
			last_object.next = arg_object
			arg_object.prev = last_object

		arg_objects.append(arg_object)
		last_object = arg_object
	return arg_objects

