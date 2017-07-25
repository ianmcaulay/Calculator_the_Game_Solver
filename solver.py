# This file will probably contain all the code



# num_moves, starting_value, target_value are ints and operations is a list of strings
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
		#remove last digit
		num=str(x)
		num=num[:-1]
		num=int(num)
	return num
		
	elif operation == "reverse":
		#do stuff-I'm assuming this means reverse the order the numbers appear in
		num=str(x)
		num=num[::-1]
		num=int(num)
	return num
	elif operation = "+/-":
		negate
	elif operation starts with +-*/:
		# TODO: make sure this works for negative numbers and more than one digit
		do stuff
	elif type(operation) == int:
		operation=str(operation)
		num=str(x)
		num+=operation
	return num

	return -1	
