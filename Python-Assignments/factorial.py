'''
Domain    : Python
Author    : Aadarshkumar Madhukar Jadhav
Created   : 12 April 2022
Problem   : Factorial of given number.
'''

def factorial(num):
    temp = 1
    if num==0:
        return "Factorial for 0 is 1"
    elif num<=0:
        return "Factorial does not exist for Negative Numbers"
    else:
        for i in range(1, num+1):
            temp = temp*i
        return temp

num = int(input("Enter a Number: "))
print(factorial(num))


# We can find factorial of any number using pre-defined module math
'''
import math
print(math.factorial(num))
'''
