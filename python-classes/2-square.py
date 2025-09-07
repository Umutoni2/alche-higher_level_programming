#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initialize a new Square."""
        self.size = size
        try:
            size > 0
        except (TypeError,ValueError):
            print(" size must be >= 0")
