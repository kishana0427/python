#altermodify.py
#This program demonstrates how to modify the column sizes of table 
import cx_Oracle
try:
	con=cx_Oracle.connect("scott/tiger@127.0.0.1/orcl")
	cur=con.cursor()
	#design the query
	amq="alter table employee modify(eno number(4),ename varchar2(15))"
	cur.execute(amq)
	print("Employee Table altred--plz verify")
except cx_Oracle.DatabaseError as db:
	print("Prob in Database: ",db)
