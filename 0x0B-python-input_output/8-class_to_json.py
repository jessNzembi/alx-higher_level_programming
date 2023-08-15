#!/usr/bin/python3
"""module documentation"""


def class_to_json(obj):
    """returns the dictionary description with simple data
    structure for json serialization of an object"""

    return obj.__dict__
