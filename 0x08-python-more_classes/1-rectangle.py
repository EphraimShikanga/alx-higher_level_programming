#!/usr/bin/python3
"""
Defines a class rectangle
"""


class Rectangle:
    """
    Representation of a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialized the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        getter for the private instance attibute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for the private instance attribute width
        """
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter for te private instance attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for the height value
        """
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

