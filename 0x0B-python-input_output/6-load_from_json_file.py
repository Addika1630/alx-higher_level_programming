#!/usr/bin/python3

"""Define a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Load an object from a JSON file.

    Args:
        filename (str): Name of the JSON file to load the object from.

    Returns:
        object: Object loaded from the JSON file.
    """

    with open(filename, "r") as f:
        obj = json.load(f)
        return obj
