#!/usr/bin/python3
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as r:
        print('Body resposne:')
        response = r.read()
        print('\t- type: {}'.format(type(response)))
        print('\t- content: {}'.format(response))
        print('\t- utf8 content: {}'.format(response.decode('utf-8')))
