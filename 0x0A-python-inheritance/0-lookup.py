#!/usr/bin/python3
''' returns the list of available attributes and methods of an object'''


def lookup(obj):
    attributes = dir(obj)
    return attributes
