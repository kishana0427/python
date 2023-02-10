'''
Domain    : Python
Author    : Aadarshkumar Madhukar Jadhav
Created   : 12 April 2022
Problem   : Fibonacci Series
'''

# Fibonacci Series using recursion
def fibo(num):
    if num<=1:
        return num
    else:
        return fibo(num-1)+fibo(num-2)

num = int(input("Enter a Number: "))
if num<=0:
    print("Invalid Number for Fibonacci Series")
else:
    print("Fibonacci Series: ", end="")
    for i in range(num):
        print(fibo(i), end=" ")


# Fibonacci series
'''
def fibo_series(num):
    i=1
    n1, n2 = 0, 1
    while i<=num:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        i+=1
fibo_series(num)
'''


# Fibonacci Series within given Number
'''
def fibo_series(num):
    i1, i2 = 0, 1
    print("Fibonacci Series: ")
    while i1<=num:
        print(i1, end=" ")
        i3=i1+i2
        i1=i2
        i2=i3
fibo_series(num)
'''

