#!/usr/bin/python3
"""Define a locked class"""


class LockedClass:
    """
    To prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
