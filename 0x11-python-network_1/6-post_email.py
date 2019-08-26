#!/usr/bin/python3
import requests
from sys import argv
if __name__ == "__main__":
    url = argv[1]

    r = requests.port(url, data={'email': argv[2]})
    print(r.text)
