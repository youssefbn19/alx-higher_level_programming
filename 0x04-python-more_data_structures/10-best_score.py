#!/usr/bin/python3
def best_score(a_dictionary):
    from functools import reduce

    a_dict = a_dictionary
    if a_dict is not None:
        best_score = reduce(
                         lambda k1, k2: k1 if a_dict[k1] > a_dict[k2] else k2,
                         list(a_dict))
        return best_score
    else:
        return None
