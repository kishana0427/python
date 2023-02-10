#empunpick.py
#This Programsgets employee record from file by using un-pickling concept by with load() of pickle
import pickle
try:
	with  open("emp.info","rb") as fp:
		print("-"*40)
		print("\tE m p l y e e  D e t a i l s")
		print("-"*40)
		print("\tEmpNo\tEmpName\tEmp Sal")
		print("-"*40)
		while(True):
			try:
				record=pickle.load(fp)
				for val in record:
					print("\t{}".format(val),end="   ")
				print()
			except EOFError:
				print("-"*40)
				break
except FileNotFoundError:
	print("File does not exists:")
