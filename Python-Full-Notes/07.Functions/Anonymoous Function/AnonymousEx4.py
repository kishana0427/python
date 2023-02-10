#AnonymousEx4.py

maxvalue=lambda lst:max(lst)

#main program
print("Enter List of values separated by space:")
lst=[int(x) for x in input().split()]
res=maxvalue(lst)
print("Biggest={}".format(res))