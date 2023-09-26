#!/usr/bin/python3
"""Define class Square here."""


class Square:
    """Represent a square here."""

    def __init__(self, size=0):
        """Initialize new Square.

        Args:
            size (int): Size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("The size must be an integer")
        elif size < 0:
            raise ValueError("The size must be >= 0")
        self.__size = size
