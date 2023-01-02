#!/usr/bin/python3
def print_last_digit(number):
    abc = ""
    lst = number % 10
    if number < 0:
        lst = lst - 10
    return lst
