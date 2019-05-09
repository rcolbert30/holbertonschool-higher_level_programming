#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i, j in enumerate(new_list):
        if j == search:
            new_list[i] == replace
        return new_list
