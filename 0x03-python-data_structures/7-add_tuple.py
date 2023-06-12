#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    while len(tuple_a) < 2:
        tuple_a += 0,
    while len(tuple_b) < 2:
        tuple_b += 0,
    new_tuple = ()
    for indx in range(0, 2):
        new_tuple += (tuple_a[indx] + tuple_b[indx]),
    return new_tuple
