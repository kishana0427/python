#logindemo.py
from verifier import loginprocess
from logindet import LoginError
while(True):
	uname=input("Enter User Name:")
	pswd=input("Enter Password:")
	try:
		loginprocess(uname,pswd)	
	except LoginError:
		print("Ur User Name / Pwd is wrong try again")
		ch=input("Do want to login again:")
		if(ch=="no"):
			exit()
	else:
		exit()
	

