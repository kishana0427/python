'''
Domain    : Python
Author    : Aadarshkumar Madhukar Jadhav
Created   : 12 April 2022
Problem   : Maximum and Minimum Number from List
'''

# list to define Minimum and Maximum from list
l=[23,12,43,645,12,123,0,1000]

# We can find maximum and minimum from list using pre-defined function max() and min()
res1, res2 = min(l), max(l)
print("Min: ", res1, "Max: ", res2)


# Find Minimum and Maximum Number from list using reduce() function
import functools
def maxmin(lst):
    min = functools.reduce((lambda a,b : a if a<b else b),lst)
    max = functools.reduce((lambda a,b :a if a>b else b), lst)
    print("Min: ", min, "Max: ", max)
# function call of maxmin() function
maxmin(l)


# programmer defined min() and max() functions
def min_num(lst):
    temp = None
    for i in lst:
        if temp is None or i<temp:
            temp=i
    print("Min: ", temp)

def max_num(lst):
    temp = None
    for i in lst:
        if temp is None or i>temp:
            temp=i
    print("Max: ", temp)
# min() and max() Function calls
min_num(l)
max_num(l)
