#studex2.py
class Student:pass


#main program
s1=Student()
s1.sno=int(input("Enter First  Student Number:"))
s1.sname=input("Enter First Student Name:")
print("---------------------------------------------")
s2=Student()
s2.sno=int(input("Enter Second  Student Number:"))
s2.sname=input("Enter Second Student Name:")
s2.cname=input("Enter second student college name:")
print("------------------------------------------------------")
print("First Student Number:{}".format(s1.sno))
print("First Student Name:{}".format(s1.sname))
print("-----------------------------------------------------")
print("Second Student Number:{}".format(s2.sno))
print("Second Student Name:{}".format(s2.sname))
print("Second Student College Name:{}".format(s2.cname))
print("-----------------OR------------------------------------")
print("First stud info={}".format(s1.__dict__))
print("Second stud info={}".format(s2.__dict__))
print("-----------------OR------------------------------------")
print("First Student Information:")
for k,v in s1.__dict__.items():
	print("\t{}--->{}".format(k,v))
print("Number of values in s1 object=", len(s1.__dict__))
print("----------------------------------------------------------------")
print("Second Student Information:")
for k,v in s2.__dict__.items():
	print("\t{}--->{}".format(k,v))
print("Number of values in s2 object=", len(s2.__dict__))