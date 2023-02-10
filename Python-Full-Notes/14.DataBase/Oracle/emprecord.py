#emprecord.py--file name and treated as module name
#this program inserts employee record into employee table dynamically
import cx_Oracle
def   recordinsert():
	try:
		con=cx_Oracle.connect("scott/tiger@127.0.0.1/orcl")
		cur=con.cursor()
		#accept employee details
		while(True):
			empno=int(input("Enter Employee Number:"))
			ename=input("Enter Employee Name:")
			esal=float(input("Enter Employee Salary:"))
			dsg=input("Enter employee Deisgnation:")
			cname=input("Enter employee company name:")
			#design the query
			#diq="insert into employee values(%d,'%s',%f,'%s','%s')"
			#cur.execute(diq %(empno,ename,esal,dsg,cname))
			#OR
			cur.execute("insert into employee values(%d,'%s',%f,'%s','%s')" %(empno,ename,esal,dsg,cname))
			con.commit()
			print("-"*50)
			print("{} record inserted into employee table:".format(cur.rowcount))
			print("-"*50)
			ch=input("Do u want to insert another record(yes/no):")
			if(ch=="no"):
				break
			if(ch!="yes"):
				print("Plz learn Typing and Reading:")

	except cx_Oracle.DatabaseError as db:
		print("Prob in Database:",db)
