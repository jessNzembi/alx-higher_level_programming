#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = (number - (10 * int(number / 10))) 
if last > 5:
    msg = "and is greater than 5"
elif last == 0:
    msg = "and is 0"
else:
    msg = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last} {msg}")
