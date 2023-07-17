#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not type(my_list) is list:
        return
    reversed_list = list(reversed(my_list))
    for item in reversed_list:
        print("{:d}".format(item))
