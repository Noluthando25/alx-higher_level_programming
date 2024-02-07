#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize the new rectangle."""
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the width of a rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be >= 0.")
        self._width = value

    @property
    def height(self):
        """Set the height of a rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be >= 0.")
        self._height = value
