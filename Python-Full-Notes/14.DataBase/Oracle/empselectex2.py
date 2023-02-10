#empselectex2.py---fetchmany()
import cx_Oracle
def  selectrecords():
	con=cx_Oracle.connect("scott/tiger@localhost/orcl")
	cur=con.cursor()
	#design the query and execute
	sq="select * from employee"
	cur.execute(sq)
	records=cur.fetchmany(3)
	for record in records:
		for val in record:
			print("{}\t".format(val),end=" ")
		print()

#main program
selectrecords()