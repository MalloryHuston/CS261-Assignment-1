# Course: CS261 - Data Structures
# Student Name: Mallory Huston
# Assignment: 1, Part 3
# Description: Implements the matrix_add() function as described in the given specifications


def matrix_add(a: [[]], b: [[]]) -> [[]]:
    """
    Adds the given matrices and returns the results
    """
    # As we can assume, all rows will have the same number of integers
    # Therefore, we only need to guard against matrices with different dimensions
    if len(a) != len(b):
        return None

    # Initializes the results list that will be returned
    results = []

    # Initializes row and element tracking variables
    current_row = 0
    current_el = 0

    # Iterates the columns and elements in the given matrix a
    for row in a:
        # Initializes a new results row
        current_results_row = []

        for el in row:
            # Adds together the current element of matrix a to the
            # corresponding element in matrix b and insert it at the
            # same element location in the current results row
            val = el + b[current_row][current_el]
            current_results_row.insert(current_el, val)
            # Iterates the tracking element variable to correspond with
            # the current element of matrix a
            current_el += 1

        # After iterating all elements in the current for for matrix a,
        # then it inserts the resulting results row into results.
        results.insert(current_row, current_results_row)

        # Iterates current row to correspond with the current row of
        # matrix a and reset the tracking element variable to 0
        current_row += 1
        current_el = 0

    # After iterating all rows and elements of a, then it returns the resulting matrix
    return results


# BASIC TESTING
if __name__ == "__main__":
    # example 1
    m1 = [[1, 2, 3], [2, 3, 4]]
    m2 = [[5, 6, 7], [8, 9, 10]]
    m3 = [[1, 2], [3, 4], [5, 6]]

    print(matrix_add(m1, m2))
    print(matrix_add(m1, m3))
    print(matrix_add(m1, m1))
    print(matrix_add([[]], [[]]))
    print(matrix_add([[]], m1))
