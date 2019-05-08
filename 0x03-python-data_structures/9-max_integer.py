#!/usr/bin/python3
def max_integer(my_list=[]):
    _max = my_list[0]
    for l in my_list:
        if l > _max:
            _max = l
        elif l < _max:
            l += 1
        elif not my_list:
            return None
        else:
            return (my_list[l])
