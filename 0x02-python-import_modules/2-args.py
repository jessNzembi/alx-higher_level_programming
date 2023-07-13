#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = len(sys.argv) - 1
    if count == 1:
        print("{} argument:".format(count))
    elif count == 0:
        print("{} arguments.".format(count))
    else:
        print("{} arguments:".format(count))

    if count != 0:
        num = 1
        for i in sys.argv[1:]:
            print("{}: {}".format(num, i))
            num += 1
