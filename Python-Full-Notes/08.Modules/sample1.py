#sample1.py---file name-----acts as Module name--->sample1.cpython310.pyc
def  simpleint():
	p=float(input("Enter Principle Amount:"))
	t=float(input("Enter Time:"))
	r=float(input("Enter Rate of Interest :"))
	#cal si
	si=(p*t*r)/100
	print('-'*40)
	print("Principle Amount:{}".format(p))
	print("Time:{}".format(t))
	print("Rate of Interest:{}".format(r))
	print("Simple Interest:{}".format(si))
	print('-'*40)

