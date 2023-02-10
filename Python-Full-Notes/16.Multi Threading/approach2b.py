#approach2b.py
import time
from threading import Thread
class MulTable(Thread):
	#don't define constructor in sub class of thread class
	def  setvalue(self):
		self.n=int(input("Enter a number:"))
	def  run(self):
		self.setvalue()
		if(self.n<=0):
			print("{} is invalid input".format(self.n))
		else:
			print("-"*50)
			print("Mul table for {}".format(self.n))
			print("-"*50)
			for i in range(1,11):
				print("\t{} x {}={}".format(self.n,i,self.n*i))
				time.sleep(1)
			print("-"*50)
#main program
mt=MulTable()
mt.start()


