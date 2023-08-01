#!/usr/bin/python3
""" class square"""


class Square:
    """ class square"""
    def __init__(self, size=0, position=(0, 0)):
        """ instantation of size"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ gets the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """gets the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value[:]

    def area(self):
        """ returns the area"""
        return self.__size ** 2

    def my_print(self):
        """prints the square with #"""
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
