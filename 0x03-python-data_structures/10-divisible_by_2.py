#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multi_two = []
    if my_list:
        for num in my_list:
            if num % 2 == 0:
                multi_two.append(True)
            else:
                multi_two.append(False)
    return multi_two
