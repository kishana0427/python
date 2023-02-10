#empselectex3.py---fetchall()
import cx_Oracle
def  selectrecords():
	con=cx_Oracle.connect("scott/tiger@localhost/orcl")
	cur=con.cursor()
	#design the query and execute
	sq="select * from employee"
	cur.execute(sq)
	print("-"*60)
	for cname in [cnames[0] for cnames in cur.description]:
		print("{}\t".format(cname),end=" ")
	print()
	print("-"*60)
	records=cur.fetchall()
	for record in records:
		for val in record:
			print("{}\t".format(val),end=" ")
		print()
	print("-"*60)
#main program
selectrecords()