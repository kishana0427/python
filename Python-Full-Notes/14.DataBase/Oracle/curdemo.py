#curdemo.py
#This program demonstrates how create a cursor
import cx_Oracle
con=cx_Oracle.connect("scott/tiger@localhost/orcl")
print("\nPython Program got connection from Oracle DB")
curobj=con.cursor()
print("\nPython Program Created cursor object:")
print("\nType of curobj=",type(curobj))


