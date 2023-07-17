#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    reversed_list = list(reversed(my_list))
    for item in reversed_list:
        print("{:d}".format(item))
