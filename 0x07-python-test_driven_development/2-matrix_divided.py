#!/usr/bin/python3

"""

Define a function for divides of a matrix

"""


def matrix_divided(matrix, div):
    """Division of a matrix

    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.

    Args:
       matrix: given matrix
       div: Division number for matrix

    Return: New divided matrix
    """

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) is not list or not all((type(l) is list)for l in matrix) \
        or not all((isinstance(n, (int, float))for n in l)for l in matrix) \
            or len(matrix[0]) == 0:
        raise TypeError(
                "matrix must be a matrix "
                "(list of lists) of integers/floats")
    l = len(matrix[0])
    if not all((len(x) == l)for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [list(map(lambda x: round(x / div, 2), r))for r in matrix]
