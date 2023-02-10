#divdemo.py
from operation import divop
import kvr
x=int(input("Enter First Value:"))
y=int(input("Enter Second Value:"))
try:
	result=divop(x,y)
except kvr.KvDivisionError:
	print("\nDon't Enter Zero for Den...")
else:
	print("\nDiv=",result)
finally:
	print("\nI am from finally block")