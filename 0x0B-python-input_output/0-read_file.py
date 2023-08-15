#!/usr/bin/python3
"""module containing a function that reads from a file"""


def read_file(filename=""):
    """ reads the content of filename and prints to stdout"""

    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
