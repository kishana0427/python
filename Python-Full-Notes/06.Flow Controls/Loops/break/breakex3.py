#breakex2.py
s="ROSSUM"
i=0
while(i<len(s)):
	if(i==3):
		break
	print(s[i],end=" ")
	i=i+1
print("\n----------------------------------")
for v in s[0:3]:
	print(v, end=" ")