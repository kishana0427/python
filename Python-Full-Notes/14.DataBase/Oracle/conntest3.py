#conntest1.py
import cx_Oracle
try:
	con=cx_Oracle.connect("scott/tiger@127.0.0.1/orcl")
	print("\nType  of con=", type(con))
	print("\nPython Program got connection fromn Oracle DB")
except cx_Oracle.DatabaseError:
	print("Unable to connect--plz check connection url")