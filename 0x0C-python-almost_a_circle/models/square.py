#!/usr/bin/python3
""" class square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ the class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ initialization of new square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updated attributes"""
        if args:
            attr_list = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attr_list[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ dictionary representation of a square"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

    def __str__(self):
        """string representation"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
