'''
Domain    : Python
Author    : Aadarshkumar Madhukar Jadhav
Created   : 12 April 2022
Problem   : Find how many time number/string repeated in given list
'''

def count1(list1):
    counter=0
    no = 'aadarsh'
    if no not in lst:
        print("Number/String not in list")
    else:
        for i in list1:
            res = list1.count(i)
            if (res>counter):
                counter=res
        print(f"{no} repeated {list1.count(no)} times in given list.")

lst = [12,23,'python',34,45,56,'aadarsh',23,45,12,12,23,67,78,23,'aadarsh']
count1(lst)
