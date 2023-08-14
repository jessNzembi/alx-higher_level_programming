#!/usr/bin/python3
""" module that contains Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """ instantiation of width and height"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """ computes the area"""
        return self.__width * self.__height

    def __str__(self):
        """ string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
