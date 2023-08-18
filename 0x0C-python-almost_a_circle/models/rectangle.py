#!/usr/bin/python3
""" class module"""
from .base import Base


class Rectangle(Base):
    """ defines Rectangle class which inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the value of width"""
        pass

    @property
    def height(self):
        """ height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height"""
        pass

    @property
    def x(self):
        """ x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        pass

    @property
    def y(self):
        """ y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """ sets the value of y"""
        pass
