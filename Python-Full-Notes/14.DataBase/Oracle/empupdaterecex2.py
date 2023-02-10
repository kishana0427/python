#empupdaterecex2.py
import cx_Oracle
def    empupdate():
	while(True):
		try:
			con=cx_Oracle.connect("scott/tiger@127.0.0.1/orcl")
			cur=con.cursor()
			esalp=float(input("Enter Percentage of Hike in Salary:"))
			#design the query and execute
			cur.execute("update employee set sal=sal + sal * %f" %esalp)
			con.commit()
		
			if(cur.rowcount>0):
				print("{} record updated in employee table".format(cur.rowcount))
			else:
				print("Employee Number / record does not exists:")
		except cx_Oracle.DatabaseError as db:
			print("Prob in Data base:",db)
		except ValueError:
			print("Don't enter strs / symbols / alpha-numerics for sal hike:")
		ch=input("\nDo u want repeat for updating another records(yes/no):")
		if(ch=="no"):
			break
		if(ch!="yes"):
			print("plz learn typing:")
			break

#main program
empupdate()
	
