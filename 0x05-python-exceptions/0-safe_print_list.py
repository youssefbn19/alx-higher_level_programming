#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len = 0
    try:
        for el in range(0, x):
            print("{}".format(my_list[el]), end="")
            len += 1
        print()
        return len
    except IndexError:
        print()
        return len
