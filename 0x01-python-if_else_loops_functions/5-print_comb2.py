#!/usr/bin/python3
for num in range(100):
    if num != 99:
        print("{}{}".format(num//10, num % 10), end=", ")
    else:
        print("{}{}".format(num//10, num % 10))
