#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    search_me = "https://swapi.co/api/people/?search={}".format(argv[1])
    r = requests.get(search_me)
    r_dict = r.json()
    count_ = r_dict.get('count')
    res = r_dict.get('results')
    print("Number of results: {}".format(count_))
    for a in res:
        print("{}".format(a.get("name")))
