#!/usr/bin/python3
"""This defines a base model class."""
import json
import csv
import turtle


class Base:
    ""the base model.

    It represents the "base" for all other classes in the  project .

    Attributes:
        __nb_objects (int): instantiated Bases numbers.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize a new Base.

        Args:
            id (int): The new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
