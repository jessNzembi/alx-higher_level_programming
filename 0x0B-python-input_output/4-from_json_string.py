#!/usr/bin/python3
""" module documentation"""
import json


def from_json_string(my_str):
    """function that returns an object represented by a json string
    Args:
        my_str (str): the json string
    """

    return json.loads(my_str)
