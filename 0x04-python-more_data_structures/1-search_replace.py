#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda el: replace if el == search else el, my_list))
    return new_list
