#div2.py
try:
	print("i am in try block:")
	print("---------------------------------")
	a=input("Enter First Value:")	
	b=input("Enter Second Value:")
	n1=int(a)
	n2=int(b)
	n3=n1/n2
except ZeroDivisionError:
	print("\nDON'T ENTER ZERO FOR DEN...")
except ValueError:
	print("\nDon't enter Strs / symbols / alpha-numerics")
else:
	print("=======================")
	print("val of n1={}".format(n1))
	print("val of n2={}".format(n2))
	print("Div={}".format(n3))
	print("=======================")
finally:
	print("========================")
	print("\nI am from finally block")