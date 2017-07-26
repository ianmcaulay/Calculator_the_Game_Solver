# This file will probably contain all the code



# num_moves, starting_value, target_value are ints and operations is a list of strings
def solve(num_moves, starting_value, target_value, operations):

    return -1

def test_apply_operation():
    # TODO: add exponential because I think that can happen as well
    test_cases = [(123, "back"), (123, "reverse"), (1, "+2"), (5, "-3"), (6, "*2"), (4, "3")]
    expecteds = [12, 321, 3, 2, 12, 43]
    for case in range(len(test_cases)):
        actual = apply_operation(test_cases[case][0], test_cases[case][1])
        if actual != expecteds[case]:
            print("failed for case " + str(test_cases[case]) + " with expected output " 
                + str(expecteds[case]) + " but actual output " + str(actual))

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
    elif operation.startswith(("+", "-", "*", "/")):
    if operation.startswith("+"):
        operation=int(operation[1:])
        x+=operation
    return x    
    if operation.startswith("-"):
        operation=int(operation[1:])
        x=x-operation
    return x
    if operation.startswith("*"):
        operation=int(operation[1:])
        x=x*operation
    return x
    if operation.startswith("/"):
        operation=int(operation[1:])
        x=x/operation
    return x
        # TODO: make sure this works for negative numbers and more than one digit
        do stuff
    elif type(operation) == int:
        operation=str(operation)
        num=str(x)
        num+=operation
    return num

    return -1   
