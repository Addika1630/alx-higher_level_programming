#!/usr/bin/python3
"""
 divides 2 integers and prints the result.
    """


def safe_print_division(a, b):
    try:
        x = a / b
    except (TypeError, ZeroDivisionError):
        x = None
    finally:
        print("Inside result: {}".format(x))
        return x
