#!/usr/bin/python3
"""Defines a cleass and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited."""
    if isinstance(obj, a_class):
        return True
    return False
