#!/usr/bin/python3

"""Defines a JSON-to-object function"""
import json


def from_json_string(my_str):
    """Convert a JSON string to the corresponding Python data structure object.

    Args:
        my_str: The JSON string to be deserialized.

    Returns:
        object: Python data structure object represented by the JSON string.
    """

    return json.loads(my_str)
