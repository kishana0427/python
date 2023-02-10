#databasecreateex.py
import mysql.connector  # step-1
try:
	con=mysql.connector.connect(host="localhost",
														user="root",
														passwd="root")   # step-2
	cur=con.cursor()#step-3
	dbc="create database ammerpet"
	cur.execute(dbc)
	print("\ndatabase created in MySQL--plz verify")
except mysql.connector.DatabaseError as db:
	print("Connection problem in MYSQL:",db)