#!/usr/bin/python3

"""Define a function that return JSON"""
import json


def to_json_string(my_obj):
    """A function that returns the JSON representation of an
       object (string):

    Args:
        my_obj: The object to be serialized to JSON.

    Returns:
        str: The JSON representation of the object as a string.
    """

    return json.dumps(my_obj)
