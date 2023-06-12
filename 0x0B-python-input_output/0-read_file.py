#!/usr/bin/python3

"""Define a function that reads text file"""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout:

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
