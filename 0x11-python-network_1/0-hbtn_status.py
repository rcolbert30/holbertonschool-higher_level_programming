#!/usr/bin/python3
'''Displays websites info using urllib'''

from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen("https://intranet.hbtn.io/status") as response:
        info = response.read()
        utf = info.decode("utf-8")
        print("Body response:")
        print("\t- type: {}".format(type(info)))
        print("\t- content:{}".format(info))
        print("\t- utf8 content: {}".format(utf))
