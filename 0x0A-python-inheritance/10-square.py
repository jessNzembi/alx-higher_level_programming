#!/usr/bin/python3
""" module that contains Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inherits from Rectangle class"""

    def __init__(self, size):
        """ instantiation of size"""

        self.integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)

    def area(self):
        """ computes the area"""
        return self.__size ** 2
