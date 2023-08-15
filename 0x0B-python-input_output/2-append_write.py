#!/usr/bin/python3
""" contains a function that appends to a file"""


def append_write(filename="", text=""):
    """ function that appends text to a file"""

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
