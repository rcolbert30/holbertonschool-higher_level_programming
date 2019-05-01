#!/usr/bin/python3
def print_last_digit(number):
    remainder = number % 10
    negative = -number % 10
    if number >= 0:
        print ("{:d}".format(remainder), end="")
    else:
        print ("{:d}".format(negative), end="")
    return negative
