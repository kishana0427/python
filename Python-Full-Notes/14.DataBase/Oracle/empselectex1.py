#empselectex1.py
import cx_Oracle
def  selectrecords():
	con=cx_Oracle.connect("scott/tiger@localhost/orcl")
	cur=con.cursor()
	#design the query and execute
	sq="select * from employee"
	cur.execute(sq)
	while(True):
		rec=cur.fetchone()
		if(rec!=None):
			for val in rec:
				print("{}\t".format(val),end=" ")
			print()
		else:
			break
#main program
selectrecords()