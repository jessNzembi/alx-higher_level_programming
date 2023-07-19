#!/usr/bin/python3
def weight_average(my_list=[]):
    average = sum([x * y for x, y in my_list]) / sum([y for x, y in my_list])
    return average
