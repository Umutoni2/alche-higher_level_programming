#!/usr/bin/python3
"""This module defines the Square class."""


class Square:
    """Defines a square with a private size attribute."""

    def __init__(self, size=0):
        """Initializes a new Square instance."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
