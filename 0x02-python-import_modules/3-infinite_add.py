#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{:d}".format(sum(int(l) for l in argv[1:])))

