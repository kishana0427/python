#DBExample.py
import cx_Oracle
class OOpswithDB:
	def    records(self,tname):
		try:
			con=cx_Oracle.connect("scott/tiger@localhost/orcl")
			cur=con.cursor()
			records=cur.execute("select * from %s" %tname)
			print("-"*40)
			for cname in [cnames[0] for cnames in cur.description]:
				print("\t{}".format(cname),end=" ")
			print()
			print("-"*40)
			for record in records:
				for val in record:
					print("\t{}".format(val),end=" ")
				print()
			print("-"*40)
		except cx_Oracle.DatabaseError as db:
			print("\nProblem in DB:",db)
#main program
tname=input("Enter Table Name:")
od= OOpswithDB()
od.records(tname)

