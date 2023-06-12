#!/usr/bin/python3

"""Defines a class Student"""


class Student():
    """A Student class that defines a Student
    """
    def __init__(self, first_name, last_name, age):
        """Instantiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """

        if (type(attrs) is list and
                all(type(el) == str for el in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
