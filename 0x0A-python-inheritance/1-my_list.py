#!/usr/bin/python3
"""A class that inherits from another"""


class MyList(list):
    """inherits from list class"""

    def print_sorted(self):
        """prints the list in ascending order"""

        print(sorted(self))
