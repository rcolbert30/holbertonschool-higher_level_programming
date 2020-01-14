#!/usr/bin/python3
'''
fetches info only using request
'''
from requests import get


if __name__ == "__main__":
    req = get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
