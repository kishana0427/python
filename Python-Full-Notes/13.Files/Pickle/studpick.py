#studpick.py
import pickle
with open("stud.info","ab") as fp:
	while(True):
		print("-"*40)
		sno=int(input("Enter Student Number:"))
		sname=input("Enter Student Name:")
		marks=float(input("Enter Student Marks:"))
		#create an empty list
		lst=[]
		lst.append(sno)
		lst.append(sname)
		lst.append(marks)
		#save lst data in a file
		pickle.dump(lst,fp)
		print("-"*40)
		print("Student Data Saved in a File:")
		print("-"*40)
		ch=input("Do u want to insert another student record(yes/no):")
		if(ch=="no"):
			break
		if(ch!="yes"):
			print("\nPlz learn Typing!")
			break




