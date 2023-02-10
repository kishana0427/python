#payslip.py
eno=int(input("Enter Employee Number:"))
ename=input("Enter Employee Name:")
basicsal=float(input("Enter Basic Salary of employee:"))
if(basicsal<=0):
	print("Invalid salary:")
else:
	if(basicsal>=10000):
		da=basicsal*(20/100)
		ta=basicsal*(15/100)
		hra=basicsal*(15/100)
		ma=basicsal*(5/100)
		gpf=basicsal*(2/100)
		lic=basicsal*(2/100)
	else:
		da=basicsal*(30/100)
		ta=basicsal*(25/100)
		hra=basicsal*(20/100)
		ma=basicsal*(10/100)
		gpf=basicsal*(1/100)
		lic=basicsal*(1/100)
	netsal=(basicsal+da+ta+hra+ma)-(gpf+lic)
	print("*"*50)
	print("Employee Number:{}".format(eno))
	print("Employee Name:{}".format(ename))
	print("Employee Basic Salary:{}".format(basicsal))
	print("Employee DA:{}".format(da))
	print("Employee TA:{}".format(ta))
	print("Employee HRA:{}".format(hra))
	print("Employee MA:{}".format(ma))
	print("Employee GPF:{}".format(gpf))
	print("Employee LIC:{}".format(lic))
	print("-"*50)
	print("Net Salary:{}".format(netsal))
	print("*"*50)







