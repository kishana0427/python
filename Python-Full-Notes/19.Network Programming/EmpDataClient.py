#This program receives Emp Name, Sal,Designation and Comp Name from Server side program by connecting to employee table 
#EmpDataClient.py----Program-(A)
import socket
while(True):
	s=socket.socket()
	s.connect(("127.0.0.1",8888))
	print("CSP Connected to SSP:")
	eno=input("\nEnter Employee Number :")
	s.send(eno.encode())
	emprec=s.recv(1024).decode()
	print("Employee data: {}".format(emprec))
	ch=input("\nDo u want to continue(yes/no):")
	if(ch=="no"):
		print("Thanks for using this program:")
		break
	




