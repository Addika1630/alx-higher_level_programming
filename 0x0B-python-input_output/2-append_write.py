#!/usr/bin/python3

"""Define a function that append text"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file (UTF8) and
       returns the number of characters added:

    Args:
        filename (str): The name of the file to which text will be appended.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added.
    """

    with open(filename, "a", encoding="utf-8") as f:
        nb_characters = f.write(text)
        return nb_characters
