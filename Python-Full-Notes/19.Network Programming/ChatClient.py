#This Program considered as Client Side Program, It Sends the Messages Server  Side Program and gets Answer as Response by client suide Program from server side program
#ChatClient.py-----Program-(B)
import socket,sys
while(True):
	s=socket.socket()
	s.connect( ("localhost",9999) )
	csdata=input("Client-->")
	if(csdata.lower()=="quit") :
		s.send("Bye Server, I have some work!".encode())
		sys.exit()
	else:
		s.send(csdata.encode())
		ssdata=s.recv(1024).decode()
		print("Server-->{}".format(ssdata))








