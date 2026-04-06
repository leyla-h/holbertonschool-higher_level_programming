#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for i in range(len(roman_string)):
        val = d.get(roman_string[i], 0)
        next_v = d.get(roman_string[i + 1], 0) if i + 1 < len(roman_string) else 0
        if val < next_v:
            res -= val
        else:
            res += val
    return res
