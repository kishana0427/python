#empselectex1.py
import mysql.connector  # step-1
def  selectrecords():
	try:
		con=mysql.connector.connect(host="localhost",
															user="root",
															passwd="root",
															database="batch11am")   # step-2
		cur=con.cursor()#step-3
		sal=float(input("Enter the salary of the employee: "))
		cur.execute("select * from employee where sal>%f" %sal)
		#print column names
		print("-"*50)
		for cname in [cnames[0] for cnames in cur.description]:
			print("{}\t\t".format(cname),end=" ")
		print()
		print("-"*50)
		records=cur.fetchall()
		if(len(records)==0):
			print("No Records Found with that Salary:")
		else:
			for record in records:
				for val in record:
					print("{}\t\t".format(val),end=" ")
				print()
			print("-"*40)
	
	except mysql.connector.DatabaseError as db:
		print("Problem in MYSQL:",db)

#main program
selectrecords()