#!/usr/bin/python3
"""Defines the inherited list."""

class MyList(list):
    """Implements sorted printing."""
    def print_sorted(self):
        """Print the list in sorted ascending order."""
        print(sorted(self))
