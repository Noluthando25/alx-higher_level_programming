#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    # If a tuple is smaller than 2, pad it with zeros
    while len(tuple_a) < 2:
        tuple_a += (0,)
    while len(tuple_b) < 2:
        tuple_b += (0,)

    # Calculate the sum of each element in the tuples
    sum_a = tuple_a[0] + tuple_b[0]
    sum_b = tuple_a[1] + tuple_b[1]

    return (sum_a, sum_b)
