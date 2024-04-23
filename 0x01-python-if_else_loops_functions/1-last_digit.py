#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = str(number)
lg = n[-1]
slg = str(lg)

if (lg > 5):
    if (number >= 0):
        print("Last digit of " + n + " is " + slg + " and is greater than 5")
    elif (number < 0):
        print("Last digit of " + n + " is -" + slg + " and is greater than 5")      
elif (lg == 0):
    print("Last digit of " + n + " is " + slg + " and is 0")
elif (lg < 6 and not 0):
    if (number > 0):
        print("Last digit of " + n + " is " + slg + " and is less than 6 and not 0")
    elif (number < 0):
        print("Last digit of " + n + " is -" + slg + " and is less than 6 and not 0")