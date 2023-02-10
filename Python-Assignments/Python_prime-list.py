'''
Domain    : Python
Author    : Aadarshkumar Madhukar Jadhav
Created   : 11 April 2022
Problem   : prime number list
'''

def primeLst(num):
    l=[]
    for i in range(2, num+1):
        prime = True
        for j in range(2,i):
            if i%j==0:
                prime=False
        if prime:
            l.append(i)
    print(l)

num = int(input("Enter Number for prime list: "))
primeLst(num)
