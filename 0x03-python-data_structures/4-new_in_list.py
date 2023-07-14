#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = list()
    for i in my_list:
        copy_list.append(i)
    if idx < 0 or idx > (len(my_list) - 1):
        return copy_list
    copy_list[idx] = element
    return copy_list
