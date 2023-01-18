#!/usr/bin/python3
"""file module"""


def write_file(filename="", text=""):
    """fun"""
    with open(filename, 'w') as f:
        return f.write(text)
