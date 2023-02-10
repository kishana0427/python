#empdeleterecex2.py
import cx_Oracle
def    empdelete():
	while(True):
		try:
			con=cx_Oracle.connect("scott/tiger@127.0.0.1/orcl")
			cur=con.cursor()
			empno=int(input("\nEnter Employee Number:"))
			#design the query and execute
			dq="delete from employee where eno=%d"
			cur.execute(dq %empno)
			con.commit()
			#OR 
			#cur.execute("delete from employee where eno=%d"  %empno)
			if(cur.rowcount>0):
				print("{} record deleted from employee table".format(cur.rowcount))
			else:
				print("Employee Number / record does not exists:")
		except cx_Oracle.DatabaseError as db:
			print("Prob in Data base:",db)
		except ValueError:
			print("Don't enter strs / symbols / alpha-numerics for employee no:")
		ch=input("Do u want repeat for deleting another record(yes/no):")
		if(ch=="no"):
			break
		if(ch!="yes"):
			print("plz learn typing:")
			break

#main program
empdelete()
	
