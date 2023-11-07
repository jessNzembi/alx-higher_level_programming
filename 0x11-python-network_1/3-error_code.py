#!/usr/bin/python3
""" sends request to url"""

import sys
import urllib.request
from urllib.error import HTTPError


def main():
    """ main function"""

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            page = response.read()
    except HTTPError as e:
        print("Error code: ", e.code)
    else:
        print(page.decode('utf-8'))


if __name__ == "__main__":
    main()
