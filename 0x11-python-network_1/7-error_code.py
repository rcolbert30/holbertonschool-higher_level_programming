#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)

    try:
        r.raise_for_status()
    except:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
