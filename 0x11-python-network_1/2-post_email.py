#!/usr/bin/python3
import urllib.request
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    payload = urllib.parse.urlencode({'email': argv[2]})
    payload = payload.encode('ascii') # data should be bytes
    with urllib.request.urlopen(url, payload) as response:
        print(response.read().decode('utf-8'))
