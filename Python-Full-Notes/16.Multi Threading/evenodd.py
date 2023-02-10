#evenodd.py
import threading,time
class EvenOdd:
	def __init__(self,n):
		self.n=n
	def generateeven(self):
		print("Name of sub therad={}".format(threading.current_thread().name))
		if(self.n<=0):
			print("{} is invalid input:".format(self.n))
		for i in range(2,self.n+1,2):
			print("Val of Even Thread={}".format(i))
			time.sleep(1)
	def generateodd(self):
		print("Name of sub therad={}".format(threading.current_thread().name))
		if(self.n<=0):
			print("{} is invalid input:".format(self.n))
		for i in range(1,self.n+1,2):
			print("Val of Odd Thread={}".format(i))
			time.sleep(1)

#main program
n=int(input("Enter the Number:"))
eo=EvenOdd(n)
et=threading.Thread(target=eo.generateeven)
ot=threading.Thread(target=eo.generateodd)
#dispatch the sub threads 
et.start()
ot.start()

