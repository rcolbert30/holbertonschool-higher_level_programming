#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value is None:
        return (a_dictionary)
    else:
        _copy = a_dictionary.copy()
        for val in _copy:
            if a_dictionary[val] == value:
                del a_dictionary[val]
        return a_dictionary
