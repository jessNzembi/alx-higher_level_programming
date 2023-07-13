#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum_all = 0
    for i in sys.argv[1:]:
        sum_all += int(i)
    print("{}".format(sum_all))
