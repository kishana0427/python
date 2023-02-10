#tablecreateex.py
import mysql.connector  # step-1
def  tabcreate():
	try:
		con=mysql.connector.connect(host="localhost",
															user="root",
															passwd="root",
															database="batch11am")   # step-2
		cur=con.cursor()#step-3
		ctq="create table employee(eno int  primary key, ename varchar(10) not null,sal real not null )"
		cur.execute(ctq)
		print("Table Created in Batch11am Database--verify")
	except mysql.connector.DatabaseError as db:
		print("Problem in MYSQL:",db)

#main program
tabcreate()