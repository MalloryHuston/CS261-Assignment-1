# Course: CS261 - Data Structures
# Student Name: Mallory Huston
# Assignment: 1, Part 4
# Description: Implements the swap_pairs() function as described in the specifications


def swap_pairs(arr: []) -> []:
    """
    Swaps indexes of every 2 elements in the given list,
    leaving the final odd element in place if present
    """
    # Sets the input list length to a variable as it's used in several places
    input_length = len(arr)

    # Guards against an empty list by returning an empty list
    if input_length == 0:
        return []

    # Initializes the results list
    results = []

    # Finds the final index limit by checking if the given input length is even or odd
    # If it is odd, the upper limit will be 1 less as there is one element left over without a pair
    ending_index = input_length - (input_length % 2)
    current_index = 0  # Initialize the current index to iterate

    # As indexing is zero-based, this program iterates indexes by 2, then swaps pairs and
    # adds them to the results list
    while current_index < ending_index:
        results.insert(current_index, arr[current_index + 1])
        results.insert(current_index + 1, arr[current_index])
        current_index += 2

    # After iterating all pairs, then it adds in the last element if the list length
    # was odd and did not equal the ending index
    if ending_index != input_length:
        results.insert(current_index, arr[current_index])

    return results


# BASIC TESTING
if __name__ == "__main__":
    # example 1
    print(swap_pairs([1, 2, 3, 4, 5]))

    # example 2
    print(swap_pairs([8, 7, 6, -5, 4, 10]))

    # example 3
    print(swap_pairs([]))
