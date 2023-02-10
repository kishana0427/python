#This program extracts  Student Names and Marks from given data
#studentnamesmarks1.py
import re
gd="Ramu got 55 marks, Raju got 66 marks, Rossum got 88 marks , Gosling got 44 marks, Ritche got 89 marks and Travis got 47 mraks"
studnames=re.findall("[A-Z][a-z]+",gd)
print("List of Student Names")
print("-"*50)
for name in studnames:
	print("\t{}".format(name))
print("-"*50)
studmarks=re.findall("\d{2}",gd)
print("List of Student Marks")
print("-"*50)
for marks in studmarks:
	print("\t{}".format(marks))
print("-"*50)
print("\tStudent Names\tStudent Marks")
print("-"*50)
for name,marks in zip(studnames,studmarks):
	print("\t\t{}\t\t{}".format(name,marks))

print("-"*50)

