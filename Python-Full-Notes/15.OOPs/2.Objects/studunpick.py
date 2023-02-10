#studunpick.py
import pickle
class StudentRetrive:
	def  getstuddata(self):
		try:
			with open("stud.info","rb") as rp:
				print("-"*40)
				print("  S t u d e n t  I n f o r m a t i o n")
				print("-"*40)
				while(True):
					try:
						stuobj=pickle.load(rp)
						stuobj.dispstuddet()
					except EOFError:
						print("-"*40)
						break
		except FileNotFoundError:
			print("File does not exists:")

#main program
sr=StudentRetrive()
sr.getstuddata()