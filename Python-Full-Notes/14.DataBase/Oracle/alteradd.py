#alteradd.py
#This program demonstrates how to add the new column to the table 
import cx_Oracle
try:
	con=cx_Oracle.connect("scott/tiger@127.0.0.1/orcl")
	cur=con.cursor()
	#design the query and execute
	cur.execute("alter table employee add(cname varchar2(10))")
	print("Employee Table altred--plz verify")
except cx_Oracle.DatabaseError as db:
	print("Prob in Database: ",db)
