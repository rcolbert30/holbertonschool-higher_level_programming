#!/usr/bin/python3
def no_c(my_string):
    string = ''
    for i in my_string:
        if i not in ['c', 'C']:
            string = string + i
    return (string)

