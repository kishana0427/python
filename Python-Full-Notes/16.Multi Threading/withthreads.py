#withthreads.py
import threading
def   disp():
	print("---------------Line-3-----------------------")
	print("i am from disp():")
	print("disp()--executed by =",threading.current_thread().name)# Therad-1
	print("--------------------------------------")
def   show():
	print("--------------Line-8------------------------")
	print("i am from show():")
	print("show()--executed by =",threading.current_thread().name)# Thread-2
	print("--------------------------------------")
def   hello():
	print("----------Line--13----------------------------")
	print("i am from Hello():")
	print("hello()--executed by =",threading.current_thread().name)# Therad-3
	print("--------------------------------------")
#main program
print("-------------------------------------------")
print("main program Executed started from--Line-18")
print("main prog stmts--executed by =",threading.current_thread().name) # mainthread
#create multiple sub threads
t1=threading.Thread(target=disp)  # here t1 is called object--whose name Thread-1
t2=threading.Thread(target=show) # here t2 is called object--whose name Thread-2
t3=threading.Thread(target=hello) # here t3 is called object--whose name Thread-3
t1.name="Sanddep"
t2.name="Kiran"
t3.name="Adarsh"
#dispatch or start the threads by mainthread
t1.start()
t2.start()
t3.start()