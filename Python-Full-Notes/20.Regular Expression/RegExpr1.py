#RegExprex1.py
#This program searches for a word "Python" in given data
import re
GivenData="Python is an oop lang and Python is also Fun Prog lang"
reg="Python"
mattab=re.finditer(reg,GivenData)
print("Type of mattab=",type(mattab))# Type of mattab= <class 'callable_iterator'>
print("-"*40)
for one in mattab:
	print("Start Index:{}   End Index:{}   Value:{}".format(one.start(),one.end(),one.group()) )
print("-"*40)