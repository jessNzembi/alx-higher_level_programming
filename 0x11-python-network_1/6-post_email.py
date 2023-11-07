#!/usr/bin/python3
""" sends a POST request to url"""

import sys
import requests


def main():
    """ main function"""
    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text['email'])


if __name__ == "__main__":
    main()
