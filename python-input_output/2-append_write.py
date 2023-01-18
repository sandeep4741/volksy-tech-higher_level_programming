#!/usr/bin/python3
"""append_write module"""


def append_write(filename="", text=""):
    """Appends a string"""
    with open(filename, 'a') as f:
        return f.write(text)
