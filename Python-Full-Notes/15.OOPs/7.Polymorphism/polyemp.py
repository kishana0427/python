#emp.py
import cx_Oracle
class EmpData:
	def  getempdata(self):
		try:
			con=cx_Oracle.connect("scott/tiger@localhost/orcl")
			cur=con.cursor()
			eno=int(input("Enter Employee Number:"))
			cur.execute("select ename,sal from emp where empno=%d" %eno)
			record=cur.fetchone()
			print("-"*40)
			if(record!=None):
				for val in record:
					print("\t{}".format(val),end="")
			else:
				print("Employee Record Does not exists")
			print()
			print("-"*40)
		except cx_Oracle.DatabaseError as db:
			print("Problem in Database:",db)

#main program
eo=EmpData()
eo.getempdata()