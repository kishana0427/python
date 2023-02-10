'''
Domain    : Python
Author    : Aadarshkumar Madhukar Jadhav
Created   : 12 April 2022
Problem   : triangle pattern
'''

# Simple Pyramid Pattern
temp = " * "
def rightTriangle(num):
    for i in range(num+1):
        print(temp*i)

def downTriangle(num):
    for i in range(num,0, -1):
        print(temp*i)

def square(num):
    for i in range(num+1):
        print(temp*num)

# Function calls
num = int(input("Enter Number: "))
rightTriangle(num)
downTriangle(num)
square(num)
