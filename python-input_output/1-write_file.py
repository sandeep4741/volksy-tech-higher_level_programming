#!/usr/bin/python3
""" hello """


def write_file(filename="", text=""):
    """ no of characters in a file """

    with open(filename, "w", encoding="utf -8") as f:
        f.write(text)
        return len(text)
