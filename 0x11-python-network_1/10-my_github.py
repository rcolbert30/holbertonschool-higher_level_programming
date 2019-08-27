#!/usr/bin/python3
from requests import get
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    password = argv[2]

    try:
        request = get('https://api.github.com/user', auth=(user, password))
        print(request.jon()['id'])
    except:
        print('None')
