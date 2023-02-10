#reduceex1.py
import  functools
print("Enter List of elements separated by space:")
lst=[float(x) for x in input().split()]
res=functools.reduce(lambda k,v: k+v , lst)
print("Sum=",res)