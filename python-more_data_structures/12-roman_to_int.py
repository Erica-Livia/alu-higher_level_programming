#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman = 0
    number = 0
    roman_number = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for r in reversed(roman_string):
        number - roman_number[r]
        roman += number if roman < number * 5 else -number
    return roman
