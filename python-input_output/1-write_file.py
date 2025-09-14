#!/usr/bin/python3
"""writing a string and returns the number of characters written"""


def write_file(filename="", text=""):
    """function to write a string and return characters number of written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
