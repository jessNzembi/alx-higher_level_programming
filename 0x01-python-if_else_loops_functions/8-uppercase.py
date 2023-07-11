#!/usr/bin/python3
def uppercase(str):
    for char in str:
        upper = ord(char)
        if upper >= 97 and upper <= 122:
            upper -= 32
        print("{}".format(chr(upper)), end="")
    print("")
