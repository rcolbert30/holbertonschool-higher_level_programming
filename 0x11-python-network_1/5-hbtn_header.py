#!/usr/bin/python3
'''
sends a request, and displays the value of the variable X-Request-Id
'''

from requests import get
from sys import argv

if __name__ == '__main__':
    r = get(argv[1])
    print(r.headers.get('X-Request-Id'))
