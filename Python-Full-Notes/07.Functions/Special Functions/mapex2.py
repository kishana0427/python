#mapex2.py
# main program
"""def  updatesal(sal):
	return (sal+sal*0.025)"""

print("Enter List of salaries of employees separated Space:")
oldsallst=[int(x) for x in input().split()]
newsallst=list(map(lambda sal:sal+sal*0.025,oldsallst))
print("==============================")
print("Old Salaries\t\tNew Salaries:")
print("==============================")
for osal,nsal in zip(oldsallst,newsallst):
	print("\t{}\t\t{}".format(osal,nsal))
print("==============================")
