#!/usr/bin/python3
"""This defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    " a rectangle child class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width.
            height (int): The height .
            x (int): The x coordinate.
            y (int): The y coordinate.
            id (int): The new Rectangle identity.
        Raises:
            TypeError: If either width or height is not an int.
            ValueError: If either  width or height <= 0.
            TypeError: If either  x or y is not an int.
            ValueError: If either x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
