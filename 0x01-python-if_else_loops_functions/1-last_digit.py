#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n_str = str(number)
lg = n_str[-1]
str(lg)

if (number > 5):
    if ( number >= 0):
        print ( "Last digit of " + n_str + " is " + lg + " and is greater than 5" )
    elif ( number < 0):
        print ( "Last digit of " + n_str + " is -" + lg + " and is greater than 5" )
        
elif (number == 0):
    print ( "Last digit of " + n_str + " is " + lg + " and is 0" )
elif (number < 6 and not 0):
    if (number > 0):
        print ( "Last digit of " + n_str + " is " + lg + " and is less than 6 and not 0" )
    elif (number < 0):
        print ( "Last digit of " + n_str + " is -" + lg + " and is less than 6 and not 0" )


