#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_div = []
    for indx in range(0, list_length):
        value = 0
        try:
            value = my_list_1[indx] / my_list_2[indx]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            list_div.append(value)
    return list_div
