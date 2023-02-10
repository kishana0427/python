#approach2c.py
import time
from threading import Thread
class CharGen(Thread):
	#don't define constructor in sub class of thread class
	def  setvalue(self):
		self.line=input("Enter a Line of Text:")
	def  run(self):
		self.setvalue()
		for i in self.line:
			time.sleep(1)
			print(i)
		print()
		
#main program
ct=CharGen()
ct.start()


