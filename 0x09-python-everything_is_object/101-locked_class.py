#!/usr/bin/python3
"""Defines locked class."""


class LockedClass:
    """
    Write a class with class or attribute that
    Prevents the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """i

    __slots__ = ["first_name"]
