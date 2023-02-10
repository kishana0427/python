#AnonymousEx5.py
tempconverter=lambda celtemp: 1.8*celtemp+32
#main program
print("Enter List of values separated by space:")
celtemp=[int(x) for x in input().split()]
for ct in celtemp:
	print("celtemp({})=ForeignTemp({})".format(ct,tempconverter(ct))  )

