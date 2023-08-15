#!/usr/bin/python3
""" module documentation"""


import json

def load_from_json_file(filename):
    """ creates an object from a json file
    Args:
        filename: the json file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
