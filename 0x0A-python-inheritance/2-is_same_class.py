#!/usr/bin/python3
"""Defines a class checking function."""

def is_same_class(obj, a_class):
    """Check if an object in exactly an instance of a given class."""
    return type(obj) is a_class
