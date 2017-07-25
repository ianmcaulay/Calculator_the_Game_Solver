# This file will probably contain all the code



def solve(num_moves, starting_value, target_value, operations):

	return -1



# Not sure what the best way to represent operations is but
# I'm thinking maybe have typical strings with associated meanings.
# For example input "+5" for the plus 5 button, "*2" for times 2,
# "3" for insert the number 3, "back" for the backspace. Given
# that I've currently only seen around 25 of the levels there are
# probably others that I'm missing.
def apply_operation(x, operation):
	# Parse the operation, apply it to x, and return the result
	
	# Rough idea of what this should look like:
	if operation == "back":
		return x // 10
	elif operation starts with +-*/:
		do stuff
	elif operation is just a number:
		append that number to x

	return -1	