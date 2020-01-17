#!/usr/bin/python3
'''
takes in a letter and sends a post request to the url
with the letter as a parameter
'''
from requests import post
from sys import argv

if __name__ == "__main__":

    if len(argv) == 1:
        l = ""
    else:
        l = argv[1]
    p = {'q': l}
    r = post('http://0.0.0.0:5000/search_user', data=p)

    try:
        response = r.json()
        if len(response) == 0:
            raise KeyError()
    except KeyError:
        print("No result")
    except ValueError:
        print("Not a valid JSON")
    else:
        print("[{}] {}".format(response['id'], response['name']))
