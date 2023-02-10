#empinsertex2.py
import mysql.connector  # step-1
def  insertrecord():
	try:
		con=mysql.connector.connect(host="localhost",
															user="root",
															passwd="root",
															database="batch11am")   # step-2
		cur=con.cursor()#step-3
		#accept employee details
		while(True):
			eno=int(input("Enter Employee Number:"))
			ename=input("Enter Employee Name:")
			sal=float(input("Enter Employee Salary:"))
			#design and execute the query
			diq="insert into employee values(%d,'%s',%f)"
			cur.execute(diq %(eno,ename,sal))
			con.commit()
			print("-"*40)
			print("{} row inserted dynamically into employee table:".format(cur.rowcount))
			print("-"*40)
			ch=input("Do u want to insert another Record(yes/no):")
			if(ch=="no"):
				break
			if(ch!='yes'):
				print("Plz Learn typing :")
				break
		
	except mysql.connector.DatabaseError as db:
		print("Problem in MYSQL:",db)

#main program
insertrecord()