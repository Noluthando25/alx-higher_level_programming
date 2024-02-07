#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize the new rectangle."""
        self._width = width
        self._height = height

    @property
    def width(self):
        """Set the width of a rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Set the height of a rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
