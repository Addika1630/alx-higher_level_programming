#!/usr/bin/python3

"""
   Defines a base geometry class BaseGeometry
"""


class BaseGeometry:
    """Represent base geometry
    """

    def area(self):
        """"Area not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """alidate a parameter as an integer

        rgs:
            name: The name of the parameter.
            value: The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer". format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0". format(name))
