#!/usr/bin/python3
"""This module defines the Square class."""


class Square:
    """Defines a square with a private size attribute."""

    def __init__(self, size=0):
        """Initializes a new Square instance."""
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square to stdout using the '#' character.
        If size is 0, it prints an empty line."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
