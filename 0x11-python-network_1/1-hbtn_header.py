#!/usr/bin/python3
'''takes in a url and send a request, show X-request-id'''
from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        print(response.info()['X-Request-ID'])
