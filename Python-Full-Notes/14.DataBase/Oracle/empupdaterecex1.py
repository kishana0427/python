#empupdaterecex1.py
import cx_Oracle
def    empupdate():
	while(True):
		try:
			con=cx_Oracle.connect("scott/tiger@127.0.0.1/orcl")
			cur=con.cursor()
			empno=int(input("\nEnter Employee Number:"))
			esal=float(input("Enter Employee New Salary for its update:"))
			dsg=input("Enter Employee New Designation for its update:")
			#design the query and execute
			cur.execute("update employee set sal=%f, dsg='%s' where eno=%d" %(esal,dsg,empno))
			con.commit()
		
			if(cur.rowcount>0):
				print("{} record updated in employee table".format(cur.rowcount))
			else:
				print("Employee Number / record does not exists:")
		except cx_Oracle.DatabaseError as db:
			print("Prob in Data base:",db)
		except ValueError:
			print("Don't enter strs / symbols / alpha-numerics for employee no:")
		ch=input("\nDo u want repeat for updating another record(yes/no):")
		if(ch=="no"):
			break
		if(ch!="yes"):
			print("plz learn typing:")
			break

#main program
empupdate()
	
