#!/usr/bin/python3
def uppercase(str):
    for i in len(str):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            num = 32
        else:
            num = 0
            print("{:s}".format(ord(str[i] - num )), end="")
    print()