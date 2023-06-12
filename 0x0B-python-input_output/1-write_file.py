#!/usr/bin/python3

"""Define a function that writes a text"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file (UTF8) and
       returns the number of characters written

    Args:
        filename (str): The name of the file to be written.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written.
    """

    with open(filename, "w", encoding="utf-8") as f:
        nb_characters = f.write(text)
        return nb_characters
