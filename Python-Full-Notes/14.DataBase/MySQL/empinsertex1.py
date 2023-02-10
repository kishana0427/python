#empinsertex1.py
import mysql.connector  # step-1
def  insertrecord():
	try:
		con=mysql.connector.connect(host="localhost",
															user="root",
															passwd="root",
															database="batch11am")   # step-2
		cur=con.cursor()#step-3
		#design and execute the query.
		iq="insert into employee values(102,'sujatha',4.7) "
		cur.execute(iq)
		con.commit()
		print("{} record inserted into employee table:".format(cur.rowcount))
	except mysql.connector.DatabaseError as db:
		print("Problem in MYSQL:",db)

#main program
insertrecord()