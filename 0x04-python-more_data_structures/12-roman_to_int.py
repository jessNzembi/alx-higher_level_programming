#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return None
    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    prev_value = 0
    total = 0
    for i in reversed(roman_string):
        value = roman_dict[i]
        if value >= prev_value:
            total += value
        else:
            total -= value
        prev_value = value
    return total
