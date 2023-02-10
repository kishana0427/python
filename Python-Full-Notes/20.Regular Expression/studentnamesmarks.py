#This program extracts  Student Names and Marks from given data
#studentnamesmarks.py
import re
gd="Ramu got 55 marks, Raju got 66 marks, Rossum got 88 marks , Gosling got 44 marks, Ritche got 89 marks and Travis got 47 mraks"
studnames=re.finditer("[A-Z][a-z]+",gd)
print("List of Student Names---finditer():")
print("-"*50)
for name in studnames:
	print("\t{}".format(name.group()))
print("-"*50)
print("---------------------OR-----------------------")
studlist=re.findall("[A-Z][a-z]+",gd)
print("List of Student Names:---findall()")
print("-"*50)
for name in studlist:
	print("\t{}".format(name))
print("-"*50)

