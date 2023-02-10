#emprecordinsertex1.py
#this program inserts employee record into employee table
import cx_Oracle
try:
	con=cx_Oracle.connect("scott/tiger@127.0.0.1/orcl")
	cur=con.cursor()
	#design the query
	iq="insert into employee values(105,'Adarsh',3.3,'SE','Siemens') "
	#execute the query
	cur.execute(iq)
	con.commit()
	print("{} record inserted sucessfully in employee table:".format(cur.rowcount) )
except cx_Oracle.DatabaseError as db:
	print("Prob in Database:",db)


