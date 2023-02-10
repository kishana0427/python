#studpick.py
import pickle
from student import Student
class StudentInsert:
	def   savestuddata(self):
		with open("stud.info","ab") as fp:
			while(True):
				print("-"*40)
				#create an student object
				so=Student()
				so.getstuddet()
				#save so data in a file
				pickle.dump(so,fp)
				print("-"*40)
				print("Student Data Saved in a File:")
				print("-"*40)
				ch=input("Do u want to insert another student record(yes/no):")
				if(ch=="no"):
					break
				if(ch!="yes"):
					print("\nPlz learn Typing!")
					break


#main program
so1=StudentInsert()
so1.savestuddata()
