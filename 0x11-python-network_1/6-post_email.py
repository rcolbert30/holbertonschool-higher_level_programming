#!/usr/bin/python3
'''
sends a post to the passed URL
Displays the body of the response
'''
from requests import post
from sys import argv

if __name__ == "__main__":
    r = post(argv[1], data={'email': argv[2]})
    print(r.text)
