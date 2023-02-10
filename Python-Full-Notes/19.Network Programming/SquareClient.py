#SquareClient.py-----Program-(B)
import socket
s=socket.socket()
#step-1
s.connect( ("localhost",8558))  
print("Client Side Program Got Connection from Server Side Program:")
#step-2
n=input("\nEnter a Value for computing its square:")
s.send(n.encode())
#step-3
result=s.recv(1024).decode() # here result is the value coming from server side program
print("square({})={}".format(n,result))




