#!/usr/bin/python3
#!/usr/bin/python3
import random
from unicodedata import decimal
number = random.randint(-10000, 10000)
number_to_str = str(number)
last_digit = int(number_to_str[-1])
if last_digit > 5:
    print(f"The last digit of {number} is {last_digit} and is greater than 5")
elif last_digit < 6 and not 0:
    print(f"The last digit of {number} is {last_digit} and is less than 6 and not 0")
else:
    print(f"The last digit of {number} is {last_digit} and is 0")