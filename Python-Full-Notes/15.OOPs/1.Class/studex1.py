#studex1.py
class Student:pass


#main program
s1=Student()
print("content of s1 before adding the data=", s1.__dict__)   # { }
print("id of s1 before adding the data =",id(s1))
#add  stno,sname and marks
s1.stno=10
s1.sname="RS"
s1.marks=22.22
print("content of s1 after adding the data=", s1.__dict__)   # {-------- }
print("id of s1 after adding the data =",id(s1))
print("-----------------------------------------------------------------")
s2=Student()
print("content of s2 before adding the data=", s2.__dict__)   # { }
print("id of s2 before adding the data =",id(s2))
s2.stno=20
s2.sname="JG"
s2.marks=44.44
print("content of s2 after adding the data=", s2.__dict__)   # {-------- }
print("id of s2 after adding the data =",id(s2))
