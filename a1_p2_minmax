# Course: CS261 - Data Structures
# Student Name: Mallory Huston
# Assignment: 1, Part 2
# Description: Implementation of the min_max function as directed in the given specs.


def min_max(arr: []) -> ():
    """
    Returns the minimum and maximum values of the given list as a tuple
    """
    # Guards against an empty list being passed and immediately returns
    if len(arr) == 0:
        return None, None

    # Initializes min and max variables with the first element in the given list
    min = arr[0]
    max = arr[0]

    # Because we have set the first element of the list, we can start iterating
    # the list from index 1. We can also set the given value and the current index
    # as max or min accordingly
    for current_index in range(1, len(arr)):
        if arr[current_index] < min:
            min = arr[current_index]
            continue  # Saves an operation by skipping the next comparison

        if arr[current_index] > max:
            max = arr[current_index]

    # Returns the min and max values
    return min, max


# BASIC TESTING
if __name__ == "__main__":
    # example 1
    print(min_max([1, 2, 3, 4, 5]))

    # example 2
    print(min_max([8, 7, 6, -5, 4]))

    # example 3
    print(min_max([]))
