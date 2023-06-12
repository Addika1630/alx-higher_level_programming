#!/usr/bin/python3

"""
    Inherit from list
"""


class MyList(list):
    """A class MyList that inherits from list
    """

    def print_sorted(self):
        """Print the sorted list
        """

        print(sorted(self))
