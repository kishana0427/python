#empex2.py
class Employee:
	cname="IBM"  # Class Level Data Member

#MAIN PROGRAM
Employee.caddr="HYD" # Class Level Data Member
eo1=Employee()
#add Instance Data Members
eo1.eno=int(input("Enter First Employee Number:"))
eo1.ename=input("Enter First Employee Name:")
eo1.sal=float(input("Enter First Employee Salary:"))

eo2=Employee()
#add Instance Data Members
eo2.eno=int(input("Enter Second Employee Number:"))
eo2.ename=input("Enter Second Employee Name:")
eo2.sal=float(input("Enter Second Employee Salary:"))

eo3=Employee()
#add Instance Data Members
eo3.eno=int(input("Enter Third Employee Number:"))
eo3.ename=input("Enter Third Employee Name:")
eo3.sal=float(input("Enter Third Employee Salary:"))
print("First Employee Data")
print("----------------------------------------------")
print("Employee Number:{}".format(eo1.eno))
print("Employee Name:{}".format(eo1.ename))
print("Employee Salary:{}".format(eo1.sal))
print("Employee Comp Name:{}".format(Employee.cname))
print("Employee Comp Addr:{}".format(Employee.caddr))
print("----------------------------------------------")
print("Second Employee Data")
print("----------------------------------------------")
print("Employee Number:{}".format(eo2.eno))
print("Employee Name:{}".format(eo2.ename))
print("Employee Salary:{}".format(eo2.sal))
print("Employee Comp Name:{}".format(eo2.cname))
print("Employee Comp Addr:{}".format(Employee.caddr))
print("----------------------------------------------")
print("Third Employee Data")
print("----------------------------------------------")
print("Employee Number:{}".format(eo3.eno))
print("Employee Name:{}".format(eo3.ename))
print("Employee Salary:{}".format(eo3.sal))
print("Employee Comp Name:{}".format(eo3.cname))
print("Employee Comp Addr:{}".format(Employee.caddr))
print("----------------------------------------------")