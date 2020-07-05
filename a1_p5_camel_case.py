# Course: CS261 - Data Structures
# Student Name: Mallory Huston
# Assignment: 1, Part 5
# Description: Implements length(), input_cleanup(), is_clean_string() and camel_case()
#              functions as described in the specifications


def length(input_string: str) -> int:
    """
    Function that receives a string and returns the number
    of characters in the string.
    """
    # Initializes a counter to increment for every character
    counter = 0

    # Iterates over every letter adding 1 to the counter
    for letter in input_string:
        counter += 1

    # Returns the counter
    return counter


def is_letter(input_char: str) -> bool:
    """
    Returns True if the given character string is an English letter,
    False if not
    """
    # Guards against empty string
    if input_char == "":
        return False

    val = ord(input_char)

    # Returns false if the value is outside the ranges of value for English letters
    if val < 65 or val > 122:
        return False

    # Returns False if the value is one of the characters between
    # upper and lowercase English letters
    if 90 < val < 97:
        return False

    # Otherwise, this program then returns True as the given character is a letter
    return True


def input_cleanup(input_string: str) -> str:
    """
    Iterates the given string and lowercases any uppercase english
    letters, removes any leading or trailing non letter characters
    and converts any non letter characters into no more than one
    consecutive underscore. The resulting string is then returned.
    """
    # Initializes the results string to build on
    results = ""

    # Iterates the input string characters along with an index
    for index, char in enumerate(input_string):
        # Handles if the current character is a letter
        if is_letter(char):
            if 65 <= ord(char) <= 90:
                results += chr(ord(char) + 32)
            else:
                results += char
        # Handles if the current character is not a letter
        else:
            # Skips if it is the first character of the input string
            if index == 0:
                continue
            # Skips if it is the last character of the input string
            # after removing a trailing underscore if present
            elif index == (length(input_string) - 1):
                if length(results) > 0 and not is_letter(results[-1:]):
                    results = results[:-1]
            # Skips if the previous character of the input string was not
            # a letter to prevent consecutive underscores
            elif not is_letter(input_string[index - 1]):
                continue
            # Replaces the non letter character with an underscore
            else:
                results += "_"

    return results


def is_clean_string(input_string: str) -> bool:
    """
    Return True if the given string contains only lowercase english letters
    or underscores or is empty, and if underscores are present they are not leading,
    trailing or consecutive with other underscores. Otherwise returns False
    """
    # Returns True if the input string is empty
    if input_string == "":
        return True

    # Returns False if the first or last character in the input string is not a letter
    if not is_letter(input_string[:1]) or not is_letter(input_string[-1:]):
        return False

    # Iterates the input string characters along with its index
    for index, char in enumerate(input_string):
        # If the current character is not a lowercase letter or an underscore
        # return False
        if (ord(char) < 97 or ord(char) > 122) and char != "_":
            return False

        # If the current character is an underscore and the previous character was also an underscore return False
        if char == "_" and is_letter(input_string[index - 1]) == "_":
            return False

    # Return true if no invalid situations were found
    return True


def camel_case(input_string: str, func_is_clean, func_cleanup):
    """
    Takes an input string and two helper functions and returns the input string
    as camel case if possible to convert. Otherwise returns None
    """
    # Sanitizes the input string
    clean_input = func_cleanup(input_string)  # DO NOT DELETE / CHANGE

    # Checks if input string is ready for camelCase conversion

    if not func_is_clean(clean_input):  # DO NOT DELETE / CHANGE
        return None  # DO NOT DELETE / CHANGE

    # Initializes a results string
    results = ""

    # Initializes tracking variables
    multiple_words = False
    capitalize_next = False

    # Iterates the characters in the clean input
    for char in clean_input:
        # If the character is an underscore, then there are multiple words and
        # the next character needs to be capitalized
        if char == "_":
            multiple_words = True
            capitalize_next = True
        # If capitalize next is True, then the program will append a capitalized version of the
        # current character to the results string and reset capitalize next to False
        elif capitalize_next:
            results += chr(ord(char) - 32)
            capitalize_next = False
        # Otherwise, this program will append the current character to the results string
        else:
            results += char

    # Return None if the clean input is not multiple words as it cannot be
    # camel cased
    if not multiple_words:
        return None

    return results


# BASIC TESTING
if __name__ == "__main__":
    if __name__ == "__main__":
        test_set = ("_random_ _word_provided",
                    "@$ptr*4con_", " ran  dom  word",
                    "example    word   ", "ANOTHER_Word",
                    "__", "_ _ _", "    ", "435%7_$$", "random")

        # example 1
        for test_string in test_set:
            result = input_cleanup(test_string)
            print(length(result), result)
        print()

        # example 2
        for test_string in test_set:
            result = input_cleanup(test_string)
            print(is_clean_string(test_string), is_clean_string(result))
        print()

        # example 3
        for test_string in test_set:
            result = camel_case(test_string, is_clean_string, input_cleanup)
            print("'" + test_string + "'", "-->", result)
