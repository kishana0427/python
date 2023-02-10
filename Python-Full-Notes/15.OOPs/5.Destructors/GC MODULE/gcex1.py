#gcex1.py
import gc
print("------------------------------------------------------------")
print("Line-3-->Is Gc is Enabled / Running?=",gc.isenabled())#True
print("Hello Python Programming")
l1=[10,20,30,40]
gc.disable()
print("Line-8-->Is Gc is Enabled / Running?=",gc.isenabled())#False
print(l1)
gc.enable()
print("Line-11-->Is Gc is Enabled / Running?=",gc.isenabled())#True
print("Hello Java program")


# gc module---- enable()   disable()  isenabled() isdisbaled()