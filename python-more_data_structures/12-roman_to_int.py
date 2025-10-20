#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for ch in reversed(roman_string.upper()):
        if ch not in vals:
            return 0
        cur = vals[ch]
        if cur < prev:
            total -= cur
        else:
            total += cur
        prev = cur
    return total
