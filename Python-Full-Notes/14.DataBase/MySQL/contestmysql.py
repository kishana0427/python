#contestmysql.py
import mysql.connector  # step-1
try:
	con=mysql.connector.connect(host="localhost",
														user="root",
														passwd="root")
	print("\nPython got connection from MYSQL")
except mysql.connector.DatabaseError as db:
	print("Connection problem in MYSQL:",db)
