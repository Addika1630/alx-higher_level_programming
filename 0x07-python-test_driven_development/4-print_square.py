#!/usr/bin/python3

"""
   Define a function that prints a square with character #.
"""


def print_square(size):
    """Print a square size with # character

    Args:
        size: the width and height of the square

    Raises:
        ValueError: If size is < 0
        TypeError: If size is not an integer.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
