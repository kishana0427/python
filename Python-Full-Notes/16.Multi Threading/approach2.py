#approach2.py
from threading import Thread  # step-1
 #      (2)       (3)
class KVR(Thread):
	def  run(self):  # (4)
		print("i am from run")
		print("Name of sub/child thread=",self.name)


#main program
#step-5
k=KVR() # here k is an object of KVR and It is the sub class of Thread class
k.name="Rao"
k.start() # step-6