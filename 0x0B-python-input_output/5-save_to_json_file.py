#!/usr/bin/python3

"""Define a JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Save an object to a text file in JSON format.

    Args:
        my_obj (object): Object to be saved.
        filename (str): Name of the text file to save the object to.

    Returns:
        None
    """

    with open(filename, "w") as f:
        json.dump(my_obj, f)
