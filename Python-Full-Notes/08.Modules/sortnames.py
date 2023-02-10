#sortnames.py----file name and treated as dodule name.
def  dispnames(lst):
	print("-"*40)
	for name in lst:
		print("\t{}".format(name))
	print("-"*40)

def sortnames():
	print("Enter Name of Students separated by Space:")
	lst=[str(x) for x in input().split()]
	print("Original Order of Names:")
	dispnames(lst)
	lst.sort()
	print("Ascending Order Names:")
	dispnames(lst)
	lst.sort(reverse=True)
	print("Decending Order Names:")
	dispnames(lst)
