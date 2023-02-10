#varlengthparamex5.py
def   disp(sname, *k,crs="PYTHON"):  # here 'k' is holding Variable number of values  of <class,'tuple'>
	print("---------------------------")
	print("Name of Student:{}".format(sname))
	print("Course Name:{}".format(crs))
	for val in k:
		print("\t{}".format(val),end=" ")
	print()
	print("---------------------------")
#main program
disp("RS",10)              #  function call-1
disp("JG",10,20)         #  function call-2
disp("DR",10,20,30)	   # Function call-3
disp("Travis", "Java","Python","KVR","DS") # Function call-4
disp("Tim")
#disp("KVR",crs="Java",20,30,40,50,60,78)---#SyntaxError:pos arg follows kwd arg.
disp("KVR",20,30,40,50,60,78,crs="JAVA")