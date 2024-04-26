#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = str(number)
l = n[-1]
d =int(l)

if (d > 5 and number >= 0):
    print("Last digit of " + n + " is " + l + " and is greater than 5")
elif (d > 5 and number < 0):
    print("Last digit of " + n + " is -" + l + " and is less than 6 and not 0")      
elif (d == 0):
    print("Last digit of " + n + " is " + l + " and is 0")
elif (d < 6 and d != 0 and number > 0):
    print("Last digit of " + n + " is " + l + " and is less than 6 and not 0")
elif (d < 6 and d != 0 and  number < 0):
    print("Last digit of " + n +  " is -" + l + " and is less than 6 and not 0")

