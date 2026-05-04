#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size
