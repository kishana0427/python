#This program receives Emp number from client side program , connect employee table , reading other details of employee and send to client side program.
#EmpDataServer.py----Program-(A)
import socket
import cx_Oracle
#step-1
s=socket.socket() 
s.bind( ("127.0.0.1",8888) )
s.listen(2)
print("SSP is ready to accept any CSP Request:")
#step-2
while(True):
	try:
		conn,addr=s.accept()
		eno=int(conn.recv(1024).decode())
		#PDBC Code
		oracon=cx_Oracle.connect("scott/tiger@localhost/orcl")
		cur=oracon.cursor()
		cur.execute("select ename,sal,dsg,cname from employee where eno=%d" %eno)
		emprec=cur.fetchone()
		if(emprec==None):
			conn.send("Employee Record Does not Exists:".encode())
		else:
			conn.send(str(emprec).encode())
	except ValueError:
		conn.send("Don't Enter strs/symbols/alpha-numerics".encode())
	except cx_Oracle.DatabaseError as db:
		conn.send("Problem in Database:"+str(db).encode())







