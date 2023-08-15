#!/usr/bin/python3
""" module documentation"""


import json

def to_json_string(my_obj):
    """ function that retuns the json representation of an object
    Args:
        my_obj: the object
    """
    return json.dumps(my_obj)
