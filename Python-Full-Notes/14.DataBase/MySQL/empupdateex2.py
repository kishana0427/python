#empupdateex2.py
import mysql.connector  # step-1
def  updaterecord():
	try:
		con=mysql.connector.connect(host="localhost",
															user="root",
															passwd="root",
															database="batch11am")   # step-2
		cur=con.cursor() #step-3
		#accept employee details
		while(True):
			eno=int(input("Enter Employee Number for updating a record:"))
			hike=float(input("Enter the hike for updating salary:"))
			#design and execute the query
			cur.execute("update employee set sal=sal+sal*%f where eno=%d" %(hike/100,eno))
			con.commit()
			print("-"*40)
			if(cur.rowcount>0):
				print("{} row updated in employee table:".format(cur.rowcount))
			else:
				print("Employee Record does not exists:")
			print("-"*40)
			ch=input("Do u want to update another Record(yes/no):")
			if(ch=="no"):
				break
			if(ch!='yes'):
				print("Plz Learn typing :")
				break
	except mysql.connector.DatabaseError as db:
		print("Problem in MYSQL:",db)

#main program
updaterecord()