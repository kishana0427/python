'''
Domain    : Python
Author    : Aadarshkumar Madhukar Jadhav
Created   : 11 April 2022
Problem   : prime or not
'''

def prime(num):
    for i in range(2, num//2):
        if num%i == 0:
            print("Not prime")
            break
    else:
        print("Prime")

num = int(input("Enter a Number: "))
if num<=0:
    print("Invalid Number")
elif num==1:
    print("1 is not a composite or prime Number")
else:
    prime(num)
