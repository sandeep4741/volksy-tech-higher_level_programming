#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Square module
"""


class Square(Rectangle):
    """class inherits from Rectangle"""

    def __init__(self, size):
        """initialization method"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)
