#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for k,v in new_list.items():
        if k == search:
            v = replace
            new_list[k] = v
    return new_list
