
# num_moves, starting_value, target_value are ints and operations is a list of strings
def solve(num_moves, starting_value, target_value, operations):
    """ Example call: solve(3, 0, 18, ["*3", "+2"]) should return the moves +2, *3, *3 """

    moves = solve_helper(num_moves, starting_value, target_value, operations, [])
    if moves:
        print_moves(moves)
    else:
        print("Unable to find solution")


def solve_helper(num_moves, current_value, target_value, operations, moves_so_far):

    if current_value == target_value:
        return moves_so_far
    if num_moves < 1:
        return False

    for operation in operations:
        new_number = apply_operation(current_value, operation)
        #print(str(current_value) + " " + operation + " " + str(new_number))
        #new_moves_so_far = moves_so_far.append(operation)
        new_moves_so_far = moves_so_far + [operation]
        using_this_operation = solve_helper(num_moves - 1, new_number, target_value, operations, new_moves_so_far)
        if using_this_operation:
            return using_this_operation

    return False

def print_moves(moves):

    for move in moves:
        print("Use button " + move)


def test_apply_operation():
    # TODO: add exponential because I think that can happen as well
    test_cases = [(123, "back"), (123, "reverse"), (1, "+2"), (5, "-3"), (6, "*2"), (4, "3")]
    expecteds = [12, 321, 3, 2, 12, 43]
    for case in range(len(test_cases)):
        actual = int(apply_operation(test_cases[case][0], test_cases[case][1]))
        if actual != expecteds[case]:
            print("failed for case " + str(test_cases[case]) + " with expected output " 
                + str(expecteds[case]) + " but actual output " + str(actual))

# TODO: could add function something like format operations that standardizes operation strings so that
# people can enter stuff like x10 or *10, ^2 or **2, etc. and it will still work (while avoiding having
# to make those alternate checks in apply_operation like how multiplication is done right now)


# TODO: there are probably other operations I'm missing
def apply_operation(x, operation):
    # Parse the operation, apply it to x, and return the result
    # Rough idea of what this should look like:
    operation = str(operation) # in case user enters operation as integer (4) rather than string ("4")
    if operation == "back":
        # Remove the last digit
        num = str(x)[:-1]
        if num == "":
            num = 0
    elif operation == "reverse":
        # Reverse the order of the digits
        num = str(x)[::-1]
    elif operation == "+/-":
        num = -1 * x
    # TODO: can consider checking operation.startswith(("+", "-", "*", "/")) and
    # doing some eval thing instead of four separate if conditions
    elif operation.startswith("+"):
        operation = int(operation[1:])
        num = x + operation
    elif operation.startswith("-"):
        operation = int(operation[1:])
        num = x - operation
    elif operation.startswith("*") or operation.startswith("x"):
        num = x * int(operation[1:])
    elif operation.startswith("/"):
        num = x / int(operation[1:])
    elif operation == "sum":
        if x < 0:
            num = -1 * sum(int(digit) for digit in str(x)[1:])
        else:
            num = sum(int(digit) for digit in str(x))
    elif operation == "mirror":
        num = str(x) + str(x)[::-1]
    elif "=>" in operation:
        prev, new = operation.split("=>")
        num = str(x).replace(prev, new)
    elif operation == ">":
        num = str(x)[-1] + str(x)[1:-1]
    elif operation == "<":
        num = str(x)[1:-1] + str(x)[-1]
    else:
        try:
            int(operation)
            num = str(x) + operation
        except:
            print("unable to apply operation " + operation)
            return 1 / 0

    return int(num)
