#droptable.py
#this Program demonstrates how toi delete / drop a table
import cx_Oracle
try:
	con=cx_Oracle.connect("scott/tiger@localhost/orcl")
	cur=con.cursor()
	cur.execute("drop table student")
	print("Table droped Successfully--verify:")
except cx_Oracle.DatabaseError as db:
	print("Problem in Database:",db)
