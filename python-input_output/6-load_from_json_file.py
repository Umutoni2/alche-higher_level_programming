#!/usr/bin/python3
""" a function that creates an Object from a “JSON file”"""


import json


def load_from_json_file(filename):
    """
    Loads an object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The Python object deserialized from the JSON file.
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
