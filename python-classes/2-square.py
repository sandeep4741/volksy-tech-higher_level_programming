#!/usr/bin/python3
class Square:
    """square"""

    def __init__(self, size=0):
        """inisialazztion"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size >= 0:
            raise ValueError("size must be >= zero")
        else:
            self.__size = size
