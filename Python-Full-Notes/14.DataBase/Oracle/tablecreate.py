#tablecreate.py
#This program demonstrates how to create a table
import cx_Oracle   # step-1
try:
	con=cx_Oracle.connect("scott/tiger@localhost/orcl")  # step-2
	cur=con.cursor() # step-3
	#step-4
	tcq="create table employee (eno number(3), ename varchar2(10), sal number(8,2), dsg varchar2(10) ) "
	cur.execute(tcq)
	print("Table Create in Oracle Database successfully--verify")
except cx_Oracle.DatabaseError as db:
	print("Prob in Database:", db)
