#accept studentNo. , StudentName and Marks
while True:
    stno=int(input("Enter Roll Number : "))
    if stno>0 and stno<=100:
        break
sname=input("Enter Your Name : ")
while True:
    mmarks=int(input("Enter Marks in MATH : "))
    if mmarks>=0 and mmarks<=100:
        break
while True:
    smarks=int(input("Enter Marks in Science : "))
    if smarks>=0 and smarks<=100:
        break
while True:
    emarks=int(input("Enter Marks in English : "))
    if emarks>=0 and emarks<=100:
        break
totmarks=mmarks+smarks+emarks
percent=(totmarks/300)*100
if (mmarks<40) or (smarks<40) or (emarks<40):
    grade="FAIL"
else:
    if totmarks<=250 and totmarks>=300:
        grade="DISTINCTION"
    elif totmarks<=200 and totmarks>=249:
        grade="FIRST CLASS"
    elif totmarks<=150 and totmarks>=199:
        grade="SECOND CLASS"
    elif totmarks<=120 and totmarks>=149:
        grade="THIRD CLASS"
print("-"*50)
print("\t S T U D E N T R E P O R T C A R D")
print("-"*50)
print("\tStudent Name : {}".format(sname))
print("\tStudent Roll Number : {}".format(stno))
print("\tMarks in MATH : {}".format(mmarks))
print("\tMarks in SCIENCE : {}".format(smarks))
print("\tMarks in ENGLISH : {}".format(emarks))
print("-"*50)
print("\tTotal Marks = {}".format(totmarks))
print("\tPercentage = {}".format(percent))
print("Student  is {}".format(grade))