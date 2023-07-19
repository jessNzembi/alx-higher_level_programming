#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    uniq = list(my_set)
    sum_uniq = 0
    for i in uniq:
        sum_uniq += i
    return sum_uniq
