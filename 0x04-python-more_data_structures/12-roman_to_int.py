#!/usr/bin/python3
def roman_to_int(roman_string):
    from functools import reduce
    chk_str = isinstance(roman_string, str)
    if chk_str and roman_string:
        roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                     'D': 500, 'M': 1000}
        rom_to_int = list(map(lambda i: roman_num[i], roman_string))
        res = reduce(lambda x, y: x + y if x >= y else y - x, rom_to_int)
        return res
    return 0
