#!/usr/bin/python3
def print_last_digit(number):
    last = (number - (10 * int(number / 10)))
    if number < 0:
        last *= -1
    print("{}".format(last), end="")
    return last
