# Course: CS261 - Data Structures
# Student Name: Mallory Huston
# Assignment: 1, Part 1
# Description: Implementation of the length() and is_divisible() functions as described in Assignment 1, Part 1


def length(s: str) -> int:
    """
    Function that receives a string and returns the number of characters in the string.
    """
    # Initializes a counter to increment for every character
    counter = 0

    # Iterates over every letter adding 1 to the counter
    for letter in s:
        counter += 1

    # Returns the counter
    return counter


def is_divisible(m: int, n: int, a: int, b: int) -> []:
    """
    Determines if a range of integers starting from +n+ and iterating backwards to +m+
    inclusive are divisible by +a+ or +b+
    """
    # Checks that the given arguments are valid for the required specifications
    if input_invalid(m=m, n=n, a=a, b=b):
        return "Incorrect input"

    results = []

    # Uses the code provided by the instructor to construct the header output
    header1 = "Num"
    header2 = "\tDiv by %s and/or %s?" % (a, b)
    under1 = "-" * length(header1) + "\t"
    under2 = "-" * length(header2)

    # Appends the header rows to the results list
    results.append(header1 + header2)
    results.append(under1 + under2)

    # Sets the current value to check divisibility to +n+
    current = n

    # Checks if the current value is divisible by +a+ or +b+
    # by appending the appropriate string to the results list.
    # Increments current by -1 after calculations are complete
    while current >= m:
        row = "%s\t" % current
        divisible_by_a = (current % a == 0)
        divisible_by_b = (current % b == 0)

        if divisible_by_a and divisible_by_b:
            row += "both"
        elif divisible_by_a:
            row += "div by %s" % a
        elif divisible_by_b:
            row += "div by %s" % b
        else:
            row += "None"

        current -= 1
        results.append(row)

    # Returns the results
    return results


def input_invalid(**kwargs) -> bool:
    """
    Checks that the inputs given are valid for the required specifications.
    """
    # If any of the arguments are less than one, then it returns True
    for val in kwargs.values():
        if val < 1:
            return True

    # If m is greater than n, or a equals b, then it returns True
    if (kwargs['m'] > kwargs['n']) or (kwargs['a'] == kwargs['b']):
        return True

    # Returns False if inputs pass conditional checks as they are valid
    return False


# BASIC TESTING
if __name__ == "__main__":
    # example 1
    print(*is_divisible(2, 7, 2, 3), sep="\n")

    # example 2
    print(is_divisible(1, 20, -1, 3))
    print(is_divisible(20, 0, 100, 200))
    print(is_divisible(10, 8, 7, 2))
    print(is_divisible(3, 30, 7, 7))
