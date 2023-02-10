#studentmarksreport.py
#validation of student number
while(True):
	stno=int(input("Enter Student  Number(1---100):"))
	if(stno>0) and (stno<=100):
		break
#Accept name
sname=input("Enter student name:")
#Accept marks and validate
while(True):
	cm=int(input("Enter marks in C:"))
	if(cm>=0) and (cm<=100):
		break

while(True):
	cppm=int(input("Enter marks in CPP:"))
	if(cppm>=0) and (cppm<=100):
		break

while(True):
	pytm=int(input("Enter marks in PYTHON:"))
	if(pytm>=0) and (pytm<=100):
		break

#Validations on Marks
totmarks=cm+cppm+pytm
percentmarks=(totmarks/300)*100
#decide grade
if ((cm<40)  or  (cppm<40) or (pytm<40) ):
	grade="FAIL"
else:
	if ((totmarks>=250) and (totmarks<=300) ):
		grade="PASSED in DISTINCTION"
	elif ((totmarks>=200) and (totmarks<=249) ):
		grade="PASSED  in FIRST"
	elif ((totmarks>=150) and (totmarks<=199) ):
		grade="PASSED in SECOND"
	else:
			if ((totmarks>=120) and (totmarks<=149) ):
				grade="PASSED in THIRD"

#display Marks Report
print("*"*50)
print("\tS t u d e n t  M a r k s  R e p o r t:")
print("*"*50)
print("\tStudent Number:{}".format(stno))
print("\tStudent Name:{}".format(sname))
print("\tStudent Marks in C:{}".format(cm))
print("\tStudent Marks in CPP:{}".format(cppm))
print("\tStudent Marks in PYTHON:{}".format(pytm))
print("-"*50)
print("\tStudent Total Marks :{}".format(totmarks))
print("\tStudent Percentage of Marks:{}".format(percentmarks))
print("\tStudent Result :{}".format(grade))
print("*"*50)











