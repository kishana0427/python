#SquareServer.py-----Program-(A)
import socket
#step-1
s=socket.socket()
s.bind( ("localhost",8558))
s.listen(2)
print("Sever Side Program is ready to accept any request of client:")
while(True):
	try:
		clientcon,clientaddr=s.accept()  # step-2
		clientdata=clientcon.recv(1024).decode() # step-3
		print("Val of client at Server={}".format(clientdata))
		val=float(clientdata)
		result=val**2 #process
		clientcon.send(str(result).encode())  #step-4
	except ValueError:
		clientcon.send("Don't Enter strs/alpha-numerics/symbols".encode())









