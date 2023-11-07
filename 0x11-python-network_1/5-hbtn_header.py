#!/usr/bin/python3
"""sends a request to url"""

import requests
import sys


def main():
    """ main function"""
    url = sys.argv[1]
    r = requests.get(url)
    content = r.headers['X-Request-Id']
    print(content)


if __name__ == "__main__":
    main()
