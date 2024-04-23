#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str=str(number)
last_digit=number_str[-1]

if(number > 5):
    print("Last digit of "+ number_str + " is " + last_digit + " and is greater than 5")
elif(number == 0):
    print("Last digit of "+ number_str + " is " + last_digit + " and is 0")
elif(number < 6 and not 0):
    print("Last digit of "+ number_str + " is " + last_digit + " and is less than 6 and not 0")

    
