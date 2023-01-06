#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for i in my_list:
        if i % 2 == 0:
            print("{:d} {:s} divisible by 2".format(my_list[i], "is")
        else:
            print("{:d} {:s} not divisible by 2".format(my_list[i], "is")
