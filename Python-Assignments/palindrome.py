'''
Domain    : Python
Author    : Aadarshkumar Madhukar Jadhav
Created   : 12 April 2022
Problem   : palindrome or not palindrome
'''

def palindrome(var):
    temp = var[::-1]
    if var == temp:
        return "Palindrome"
    else:
        return "Not Palindrome"

var = input("Enter String: ")
print(palindrome(var))
