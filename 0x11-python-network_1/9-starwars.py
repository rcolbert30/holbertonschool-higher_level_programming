#!/usr/bin/python3
'''
takes in a string and sends a search request
to the Star Wars API
'''
from requests import get
from sys import argv

if __name__ == "__main__":

    if len(argv) == 1:
        letter = ""
    else:
        letter = argv[1]

    p = {'search': letter}

    try:
        r = get('https://swapi.co/api/people', params=p)
        response = r.json()
        results = response['results']
        count = response['count']
        print('Number of results: {}'.format(count))
        for i in results:
            print(i['name'])
    except Exception as error:
        print(error)
