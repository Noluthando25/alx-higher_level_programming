#!/usr/bin/python3
"""Defines a base geometry."""


class BaseGeometry:
    """Represent base geometry."""
    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a perimeter as an integer."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{name} must be greater than 0".format(name))
