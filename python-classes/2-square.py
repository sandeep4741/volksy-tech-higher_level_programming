#!/usr/bin/python3
'''square'''
class Square:
       """inisialazztion"""

    def __init__(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size >= 0:
            raise ValueError("size must be >= zero")
        else:
            self.__size = size
