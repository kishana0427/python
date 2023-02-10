#threadex1.py
import threading
#main program
tname=threading.current_thread() # gives currently executing thread
print("-"*40)
print("name of the thread in Python program=", tname.name  )#  MainThread
print("-"*40)
print("Hello Python World")
print("This is my First Python Program")
print("-"*40)
print("Number of thread in this program=",threading.active_count())# gives number of threads available in python program.
print("-"*40)

#In Python Programming main program executed by "mainthread"