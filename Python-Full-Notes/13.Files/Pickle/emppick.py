#emppick.py
#This Programs accepts employee details and save those details in a file by using pickle module with dump()-----Program-(A)
import pickle
noe=int(input("Enter How Many employee information u have:"))
if(noe<=0):
	print("{} is invalid input".format(noe))
else:
	with open("emp.info","ab") as fp:
		for i in range(1,noe+1):
				print("-"*50)
				print("Enter {} Employee Information:".format(i))
				print("-"*50)
				eno=int(input("Enter Employee Number:"))
				ename=input("Enter Employee Name:")
				esal=float(input("Enter Employee Salary:"))
				#add employee values to list object
				lst=list()
				lst.append(eno)
				lst.append(ename)
				lst.append(esal)
				#dump the list object data into the file
				pickle.dump(lst,fp)
				print("-"*50)
				print("{} Employee Data Saved in a file:".format(i))



