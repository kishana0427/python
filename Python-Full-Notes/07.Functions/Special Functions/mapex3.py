#mapex3.py
lst1=[10,20,30,40]
lst2=[100,200,300,400]
sumlist=list(map(lambda x,y:x+y ,lst1,lst2))
print("========================================")
print("First List\tSeconList\tSum List:")
print("==========================================")
for x,y,z in zip(lst1,lst2,sumlist):
	print("\t{}\t+\t{}\t=\t{}".format(x,y,z))
print("=========================================")
