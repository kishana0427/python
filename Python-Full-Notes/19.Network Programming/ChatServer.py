#This Program considered as Server Side Program, It receives the Messages from Client Side Program and Gives Answer as Response to client suide Program
#ChatServer.py-----Program-(A)
import socket
s=socket.socket()
s.bind( ("localhost",9999) )  
s.listen(1) # step-1
print("Sever Side Program is ready to accept any request of client:")
print("-"*40)
while(True):
	con,addr=s.accept()   # step-2
	csdata=con.recv(1024).decode()#step-3
	print("Client-->{}".format(csdata))
	sdata=input("Server-->")
	con.send(sdata.encode())



