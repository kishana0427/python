#approach3.py
import threading   #step-1
class Hyd:     #step-2
	def  disp(self,name):  # instance method--Step-3
		print("Hi {}, Good Morning".format(name))
	def show(self):
		print("Good Evening")
#main program
h=Hyd() # step-4
t1=threading.Thread(target=h.disp,args=(("Rossum",) )  )
t1.start()  # step-5
t2=threading.Thread(target=h.show)
t2.start()