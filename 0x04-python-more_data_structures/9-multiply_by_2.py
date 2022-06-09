#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    new_list = list(new_dict.keys())
    for k in new_list:
        new_dict[k] *= 2
    return new_dict
