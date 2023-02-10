#This program extracts  Student Names and Marks from given data file data
#studentnamesmarks2.py
import re
with open("D:\KVR-PY\stud.info","r") as fp:
	filedata=fp.read()
	studnames=re.findall("[A-Z][a-z]+",filedata)
	studmarks=re.findall("\d{2}",filedata)
	print("-"*50)
	print("\tStudent Names\tStudent Marks")
	print("-"*50)
	for name,marks in zip(studnames,studmarks):
		print("\t\t{}\t\t{}".format(name,marks))
	print("-"*50)
