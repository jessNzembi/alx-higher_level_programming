#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    new_string = ''
    for item in my_list:
        if item == 'c' or item == 'C':
            continue
        new_string += item
    return new_string
