#!/usr/bin/python3
"""function"""


def read_file(filename=""):
    """text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
