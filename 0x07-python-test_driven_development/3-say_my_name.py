#!/usr/bin/python3
"""function that prints a name"""


def say_my_name(first_name, last_name=""):
    """prints full name
    Args:
        first_name(str): the first name
        last_name(str): the last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
