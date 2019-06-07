#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    lines = 0
    with open(filename) as myFile:
        for line in myFile:
            lines += 1
            print(line, end="")
            if nb_lines == lines:
                break
