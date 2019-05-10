#!/usr/bin/python3
def roman_to_int(roman_string):
    convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    _sum = 0
    p = 0
    if not isinstance(roman_string, str) and roman_string is None:
        return (0)
    else:
        for i in roman_string:
            for d in convert:
                if i == d:
                    if p < convert[d]:
                        _sum += convert[d] - p * 2
                    else:
                        _sum += convert[d]
                    p = convert[d]
        return (_sum)
