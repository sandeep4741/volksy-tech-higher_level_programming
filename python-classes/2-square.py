#!/usr/bin/python3
class Square:
    """square"""
    def __init__(self, size=0):
        """inisialazztion"""
        self.__size__ = size
        if size != int:
            raise TypeError("size must be an integer")
        else size >= 0:
            raise ValueError("size must be greater than zero")

