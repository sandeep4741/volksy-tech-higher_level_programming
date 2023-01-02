#!/usr/bin/python3
def print_last_digit(number):
    lst = number % 10
    if number < 0:
        lst = lst - 10
    return lst
