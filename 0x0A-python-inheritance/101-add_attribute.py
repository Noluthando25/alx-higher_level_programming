#!/usr/bin/python3
"""Defines a function.."""


def add_new_attribute(obj, attr_name, attr_value):
    """Object has an attribute."""
    if hasattr(obj, attr_name):
        raise TypeError("can't add new attribute")
    else:
        obj.__setattr__(attr_name, attr_value)
