#colnames.py----
import cx_Oracle
def  colnames():
	con=cx_Oracle.connect("scott/tiger@localhost/orcl")
	cur=con.cursor()
	#design the query and execute
	sq="select * from employee"
	cur.execute(sq)
	cnames=[ colname[0]  for colname in cur.description]
	for cname in cnames:
		print("{}\t".format(cname),end=" ")
	print()
	print("=============OR================")
	for cname in  [colname[0]  for colname in cur.description]:
		print("{}\t".format(cname),end=" ")
	print()
#main program
colnames()