#FilterEx3.py
print("Enter List of elements separated by space:")
lst=[int(val) for val in input().split()]
evenlst=list(filter(lambda n : n%2==0, lst))
oddlst=tuple(filter(lambda k : k%2!=0,lst))
print("Given Elements={}".format(lst))
print("Even Elements={}".format(evenlst))
print("Odd Elements={}".format(oddlst))

