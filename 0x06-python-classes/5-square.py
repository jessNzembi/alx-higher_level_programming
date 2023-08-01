#!/usr/bin/python3
""" class square"""


class Square:
    """ class square"""
    def __init__(self, size=0):
        """ instantation of size"""
        self.__size = size

    @property
    def size(self):
        """ getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """ setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the area"""
        return self.__size ** 2

    def my_print(self):
        """prints the square with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
