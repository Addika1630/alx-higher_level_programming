#!/usr/bin/python3
# 0-add_integer.py
# Addisu Mulat  <addisu05mulat@gmail.com>

"""

    Define a function that adds two integers

"""


def add_integer(a, b=98):
    """Return the addition of two integers.
    Raises:TypeError: if either a or b is not integer or float
    Float is typecasted into integers"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
