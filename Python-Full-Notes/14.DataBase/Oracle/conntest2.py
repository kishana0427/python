#conntest.py
import cx_Oracle
kvrcon=cx_Oracle.connect("scott/tiger@localhost/orcl")
print("\nType if kvrcon=", type(kvrcon))
print("\nPython Program got connection fromn Oracle DB")
