#!/usr/bin/python3
"""Defines a rectangle subclass square."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square."""

        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
