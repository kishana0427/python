#sortnamescompre.py
print("Enter number of Names separated by space:")
names=[ val for val in input().split()]
print("-----------------------------------------")
print("Given Names:")
print("-----------------------------------------")
for name in names:
	print(name)
print("-----------------------------------------")
names.sort(reverse=True)
print("Sorted  Names--ASC order:")
print("-----------------------------------------")
for name in names:
	print(name)
print("-----------------------------------------")

