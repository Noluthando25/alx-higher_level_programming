#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import json
from sys import argv
import os.path


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []
