#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)

    if len(argv) == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument:")
        print("1: {:s}".format(argv[1]))
    else:
        print("{:d} arguments:".format(length - 1))
        for l in range(1, length):
            print("{:d}: {:s}".format(l, argv[l]))
