#!/usr/bin/python3
""" module documentation"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using json representation
    Args:
        my_obj: the object
        filename: the text file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
