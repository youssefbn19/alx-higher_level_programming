#!/usr/bin/python3
def weight_average(my_list=[]):
    from functools import reduce

    avg = 0
    if my_list:
        score_weight, weight_total = 0, 0
        for el in my_list:
            score_weight += el[0] * el[1]
            weight_total += el[1]
        avg = score_weight / weight_total

    return avg
