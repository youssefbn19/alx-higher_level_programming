#!/usr/bin/python3

for first_digit in range(0, 8):
    for last_digit in range(0, 10):
        if last_digit > first_digit:
            print("{}{}, ".format(first_digit, last_digit), end="")
else:
    print("89")
