#reduceex2.py
import  functools
print("Enter List of elements separated by space:") #10 30 20 50  40  60
lst=[float(x) for x in input().split()]
big=functools.reduce(lambda a,b: a if a>b else b, lst)
small=functools.reduce(lambda a,b: a if a<b else b, lst)
print("Biggest={}".format(big))
print("Smallest={}".format(small))
