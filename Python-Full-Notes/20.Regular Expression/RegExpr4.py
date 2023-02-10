#RegExprex4.py
#This program searches for a word "Python" in given data 
import re
GivenData="Python is an oop lang and Python is also Fun Prog lang"
reg="Python"
mattab=re.search(reg,GivenData)
if(mattab!=None):
	print("type of mattab=",type(mattab))
	print(mattab)
else:
	print("{}  does not exist in Given Data:".format(reg))
