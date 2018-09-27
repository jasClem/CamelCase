__author__ = "Jason"
# DONE
from camelCase import *
# Import functions


def main():

    camel_case_input = input("\nEnter words to camelCase (separated by spaces):  ")
    # Get user input for words to camelCase

    words_to_camelcase = camel_case_input.split(' ')
    # Separate the words by spaces

    camel_case_words = [camel_case(each_word) for each_word in words_to_camelcase]
    # Send words to turn into camelCase

    camel_case_words[0] = camel_case_words[0].lower()
    # Change first word to lowercase

    output = "".join(camel_case_words)
    # Remove spaces from words

    print(output)
    # Display camelCase words


main()
