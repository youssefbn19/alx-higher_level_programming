#!/usr/bin/python3
def roman_to_int(roman_string):
    from functools import reduce
    chk_str = isinstance(roman_string, str)
    res = 0
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                 'D': 500, 'M': 1000}
    if chk_str and roman_string:

        for char in roman_string:
            if char not in set(list(roman_num)):
                return res

        rom_to_int = list(map(lambda i: roman_num[i], roman_string))
        ln = len(rom_to_int)

        for i in range(ln):
            j = i + 1
            if j == ln:
                res += rom_to_int[i]
            elif rom_to_int[i] >= rom_to_int[j]:
                res += rom_to_int[i]
            else:
                res -= rom_to_int[i]

    return res
