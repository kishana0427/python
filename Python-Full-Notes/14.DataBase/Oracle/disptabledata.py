#disptabledata.py----
import cx_Oracle
def  tabledata():
	try:
		con=cx_Oracle.connect("scott/tiger@localhost/orcl")
		cur=con.cursor()
		#design the query and execute
		tname=input("Enter table name:")
		sq="select * from %s"
		cur.execute(sq %tname)
		print("-"*60)
		cnames=[ colname[0]  for colname in cur.description]
		for cname in cnames:
			print("{}\t".format(cname),end=" ")
		print()
		print("-"*60)
		#get the records
		records=cur.fetchall()
		for record in records:
			for val in record:
				print("{}\t".format(val),end=" ")
			print()
		print("-"*60)
	except cx_Oracle.DatabaseError as db:
		print("Prob in Database:",db)
#main program
tabledata()