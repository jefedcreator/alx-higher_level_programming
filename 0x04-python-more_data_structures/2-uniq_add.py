#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_num = set(my_list)
    num = 0
    for i in uniq_num:
        num += 1
    return num
