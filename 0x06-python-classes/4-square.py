#!/usr/bin/python3
"""Define class Square here."""


class Square:
    """Represent square here."""

    def __init__(self, size=0):
        """Initialize new square here.

        Args:
            size (int): Size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square here."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("The size must be an integer")
        elif value < 0:
            raise ValueError("The size must be >= 0")
        self.__size = value

    def area(self):
        """Return current area of the square."""
        return (self.__size * self.__size)
