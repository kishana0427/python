#colnames1.py
import cx_Oracle
def  colnames():
	try:
		con=cx_Oracle.connect("scott/tiger@localhost/orcl")
		cur=con.cursor()
		#design the query and execute
		tname=input("Enter table name:")
		sq="select * from %s"
		cur.execute(sq %tname)
		cnames=[ colname[0]  for colname in cur.description]
		for cname in cnames:
			print("{}\t".format(cname),end=" ")
		print()
		print("=============OR================")
		for cname in  [colname[0]  for colname in cur.description]:
			print("{}\t".format(cname),end=" ")
		print()
	except cx_Oracle.DatabaseError as db:
		print("Prob in Database:",db)
#main program
colnames()