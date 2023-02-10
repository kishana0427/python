#RegExprex2.py
#This program searches for a word "Python" in given data and find number of occurences.
import re
GivenData="Pythonic is an oop lang and Python is also Fun Prog lang"
reg="Python"
mattab=re.finditer(reg,GivenData)
noc=0
print("-"*40)
for one in mattab:
	print("Start Index:{}   End Index:{}   Value:{}".format(one.start(),one.end(),one.group()) )
	noc=noc+1
print("-"*40)
print("Number of Occurences of {}={}".format(reg,noc))
print("-"*40)