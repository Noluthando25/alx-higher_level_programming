#!/usr/bin/python3
"""Defines a rectangle subclass spuare."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""
    def __init__(self, size):
        """Initialize a new square."""
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return size."""
        return self.__size ** 2
