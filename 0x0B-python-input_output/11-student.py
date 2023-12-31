#!/usr/bin/python3
""" Student class module"""


class Student:
    """ Student class"""

    def __init__(self, first_name, last_name, age):
        """ instantiation with first_name, last_name and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""

        if type(attrs) is not list:
            return self.__dict__
        else:
            my_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    my_dict[key] = value
            return my_dict

    def reload_from_json(self, json):
        """ replaces all attributes of the student instance"""

        for key, value in json.items():
            setattr(self, key, json[key])
