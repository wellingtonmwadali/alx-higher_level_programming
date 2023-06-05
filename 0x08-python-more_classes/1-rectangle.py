#!/usr/bin/python3
"""define rectangle class"""


class Rectangle:
    """represent rectangle"""

    def __init__(self, width=0, height=0):
        """initialise rectangle

        args:
        width : rectangle width
        height: rectangle height
        """

        self.width = width
        self.height = height

        @property
        def width(self):
            """set rectangle width"""
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

            @property
            def height(self):
                """set the height of rectangle"""
                return self.__height

            @height.setter
            def height(self, value):
                if not isinstance(value, int):
                    raise TypeError("height must be integer")
                if value < 0:
                    raise ValueError("height must be >= 0")
                self.__height = value
