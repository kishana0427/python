#empdeleterecex1.py
import cx_Oracle
def    empdelete():
	con=cx_Oracle.connect("scott/tiger@127.0.0.1/orcl")
	cur=con.cursor()
	#design the query and execute
	dq="delete from employee where eno=100"
	cur.execute(dq)
	con.commit()
	if(cur.rowcount>0):
		print("{} record deleted successfully from employee table".format(cur.rowcount))
	else:
		print("Employee record does not exist")

#main program
empdelete()

