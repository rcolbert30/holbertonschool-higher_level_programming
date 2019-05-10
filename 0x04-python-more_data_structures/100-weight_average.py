#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    else:
        length = len(my_list)
        _sum = map(sum, my_list)
        average = _sum / length
    return (average)
