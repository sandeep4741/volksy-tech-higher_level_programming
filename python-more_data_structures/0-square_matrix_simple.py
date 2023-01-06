#!/usr/bin/python3
def square_matrix_simple(abc=[]):
    nre = []
    for i in abc:
        sd = map(lambda a: a**2, i)
        nre.append(list(sd))
    return nre
