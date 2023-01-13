#!/usr/bin/python3
"""Geometry module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class inheriting from the Rectangle class which inherits"""
    def __init__(self, size):
        """Class constructor with private attributes"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method to calculate area """
        return self.__size ** 2

    def __str__(self):
        """return string"""
        return str("[Square] {}/{}".format(self.__size, self.__size))
