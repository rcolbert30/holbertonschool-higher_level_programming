#!/usr/bin/python3
import urllib.request
from urllib.request import urlopen
from sys import argv
from urllib.error import HTTPError

if __name__ == "__main__":
    url = argv[1]

    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
