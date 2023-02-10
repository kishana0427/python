#withoutthreads.py
import threading
def   disp():
	print("---------------Line-3-----------------------")
	print("i am from disp():")
	print("disp()--executed by =",threading.current_thread().name)#mainthread
	print("--------------------------------------")
def   show():
	print("--------------Line-8------------------------")
	print("i am from show():")
	print("show()--executed by =",threading.current_thread().name)#mainthread
	print("--------------------------------------")
def   hello():
	print("----------Line--13----------------------------")
	print("i am from Hello():")
	print("hello()--executed by =",threading.current_thread().name)#mainthread
	print("--------------------------------------")
#main program
print("-------------------------------------------")
print("main program Executed started from--Line-18")
print("main prog stmts--executed by =",threading.current_thread().name) # mainthread
disp()
print("i am in main program ---Line-22")
show()
print("i am in main program ---Line-24")
hello()
print("i am in main program ---Line-26")