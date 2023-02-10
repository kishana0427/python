#FilterEx2.py
even=lambda n : n%2==0
odd=lambda k : k%2!=0

#main program
print("Enter List of elements separated by space:")
lst=[int(val) for val in input().split()]
evenlst=list(filter(even,lst))
oddlst=tuple(filter(odd,lst))
print("Given Elements={}".format(lst))
print("Even Elements={}".format(evenlst))
print("Odd Elements={}".format(oddlst))

