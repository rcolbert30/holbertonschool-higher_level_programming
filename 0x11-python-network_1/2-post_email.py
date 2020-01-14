#!/usr/bin/python3
'''
'''
from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    info = urlencode({'email': argv[2]}).encode('utf-8')
    with urlopen(argv[1], info) as response:
        print(response.read().decode('utf-8'))
