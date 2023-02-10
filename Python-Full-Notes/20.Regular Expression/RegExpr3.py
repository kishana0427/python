#RegExprex3.py
#This program searches for a word "Python" in given data and find number of occurences.
import re
GivenData="Python is an oop lang and Python is also Fun Prog lang"
reg="Python"
mattab=re.findall(reg,GivenData)
print("type of mattab=",type(mattab))
print(mattab)
print("Number of occurences of {}={}".format(reg,len(mattab)))