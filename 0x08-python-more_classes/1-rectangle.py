#!/usr/bin/python3
""" rectangle class"""


class Rectangle:
    """class Rectangle"""
    def __init__(self, width=0, height=0):
        """instantiation of width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
