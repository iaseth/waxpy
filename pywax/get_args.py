import sys

from .command_line_argument import CommandLineArgument



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

