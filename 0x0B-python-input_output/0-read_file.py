#!/usr/bin/python3


def read_file(filename=""):
    with open(filename) as f:
        data = f.read()
    print(data, end="")
