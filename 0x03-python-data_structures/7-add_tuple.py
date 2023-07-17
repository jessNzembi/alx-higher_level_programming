#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup1 = tuple_a
    tup2 = tuple_b
    if len(tuple_a) < 2:
        tup1 = tuple_a + (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tup2 = tuple_b + (0,) * (2 - len(tuple_b))
    t = (tup1[0] + tup2[0], tup1[1] + tup2[1])
    return t
