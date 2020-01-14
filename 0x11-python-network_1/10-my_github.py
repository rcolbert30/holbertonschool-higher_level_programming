#!/usr/bin/python3
'''
access the github api to display id
'''
from requests import get
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    try:
        req = get('https://api.github.com/user', auth=(user, password))
        print(req.json()['id'])
    except:
        print("None")
