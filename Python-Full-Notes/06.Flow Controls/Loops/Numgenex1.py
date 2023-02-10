#Numgenex1.py
#this program generates 1 to  n where n is +ve
n=int(input("Enter a number:"))  # n=5
if(n<=0):
	print("{} is invalid input".format(n))
else:
	i=1  # initlizatioon part
	while(i<=n):  # cond part
		print("val of i={}".format(i))
		i=i+1  # updation part
	else:
		print("\nI am from else--while--val of i=",i)
	print("\nProgram exec . Over while..else")
print("Program exec over--if..else")