#This program validates Mobile Number by using regular expressions.
#MobileNumberValid.py
import re
while(True):
	mno=input("Enter Ur Mobile Number:")
	if (len(mno)==10):
		result=re.search( "\d{10}" ,mno)                   
		if(result !=None):
			print("Ur Mobile Number is Valid:")
			break
		else:
			print("Ur Mobile Number must contain only digits\nshould not contain chars and symbols")
	else:
		print("Ur Mobile Number must contain 10 digits length only:")

