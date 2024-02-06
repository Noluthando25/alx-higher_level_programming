#!/usr/bin/python3
"""Defines a function."""


class MyInt(int):
    """Check for equality."""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
