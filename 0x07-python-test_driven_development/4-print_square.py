#!/usr/bin/python3
# 4-print_square.py
"""Defines a square-printing function."""


def print_square(size):
    """Print a square with the # character.
    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
