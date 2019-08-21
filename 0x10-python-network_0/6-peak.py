#!/usr/bin/python3

def find_peak(list_of_integers):
    max_int = None

    for i in list_of_integers:
        if max_int is None or max_int < i:
            max_int = i
    return max_int
