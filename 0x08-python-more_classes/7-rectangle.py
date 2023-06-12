#!/usr/bin/python3

"""
    Define a Rectangle Class
"""


class Rectangle:
    """Represent a rectangle class

    Args:
        width: Private
        height: Private
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Init Rectangle Class

        width: The width of rectangle
        height: The height of rectangle
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter
            Return: The width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter

        Args:
            Value : a value to set

        Raises:
            TypeError: When value is not int
            ValueError: When value is less than 0
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter
            Return: The height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Hieght setter

        Args:
            Value : a value to set

        Raises:
            TypeError: When value is not int
            ValueError: When value is less than 0
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return Rectangle Area
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """print the rectangle
            Represents the rectangle with the # character.
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = str(self.print_symbol)
        return ((symbol * self.__width + "\n")*self.__height)[:-1]

    def __repr__(self):
        """ string representation of the rectangle
        Return:
            (str) representation of the rectangle
        """

        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print message when instances deleted
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
