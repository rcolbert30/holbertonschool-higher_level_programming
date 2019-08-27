#!/usr/bin/python3
from requests import post
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        char = ""
    else:
        char = argv[1]

    request = post('http://0.0.0.0:5000/search_user', data={'q': char})

    try:
        r = request.json()
        if len(r) == 0:
            raise KeyError()
    except KeyError:
        print("No result")
    except ValueError:
        print("Not a valid JSON")
    else:
        print("[{}] {}".format(r['id'], r['name']))
