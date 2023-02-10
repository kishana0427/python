#This program extract email ids of various people where they present in a file "emails.info"
#extractmails.py
import re
try:
	with open("emails.info","r") as fp:
		emaildata=fp.read()
		studnames=re.findall("[A-Z][a-z]+",emaildata)
		emaillist=re.findall("\S+@\S+", emaildata)
		print("-"*50)
		print("Student mail list")
		print("-"*50)
		for mail in emaillist:
			print("{}".format(mail))
		print("-"*50)
		print("Student Name\tEmail-Id")
		print("-"*50)
		for names,mail in zip(studnames,emaillist):
			print("{}\t\t{}".format(names,mail))
		print("-"*50)
except FileNotFoundError:
	print("File does not exists:")