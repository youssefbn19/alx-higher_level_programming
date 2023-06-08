#!/usr/bin/python3

char_number = 97
while char_number <= 122:
    if char_number == 101 or char_number == 113:
        char_number += 1
        continue
    print("{:c}".format(char_number), end="")
    char_number += 1
