#empex1.py
class Employee:
	cname="IBM"  # Class Level Data Member

#MAIN PROGRAM
Employee.caddr="HYD" # Class Level Data Member
eo1=Employee()
#add Instance Data Members
eo1.eno=100
eo1.ename="RS"
eo1.sal=5.6

eo2=Employee()
#add Instance Data Members
eo2.eno=200
eo2.ename="JG"
eo2.sal=3.6

eo3=Employee()
#add Instance Data Members
eo3.eno=300
eo3.ename="DR"
eo3.sal=4.6
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
