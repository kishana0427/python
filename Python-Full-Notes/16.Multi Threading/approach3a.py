#approach3a.py
import threading,time
class Python:
	def  generate(self):
		print("Name of sub thread={}".format(threading.current_thread().name))
		self.n=int(input("\nEnter a number:"))
		if(self.n<=0):
			print("{} is invalid input:".format(self.n))
		else:
			print("-"*40)
			print("Numbers within:{}".format(self.n))
			print("-"*40)
			for i in range(1,self.n+1):
				print("Val of i={}".format(i))
				time.sleep(1)
			print("-"*40)

#main program
p=Python() # create an object of Programmer-defined class
t=threading.Thread(target=p.generate)
print("Name of t1=",t.name)
t.name="Rossum" #setting the user-friendly Name to the sub-therad
t.start()
