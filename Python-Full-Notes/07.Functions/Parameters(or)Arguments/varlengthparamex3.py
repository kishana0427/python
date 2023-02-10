#varlengthparamex3.py
def   disp( *k  ):  # here 'k' is holding Variable number of values  of <class,'tuple'>
	print("---------------------------")
	for val in k:
		print("\t{}".format(val),end=" ")
	print()
	print("---------------------------")

#main program
disp(10)              #  function call-1
disp(10,20)         #  function call-2
disp(10,20,30)	   # Function call-3
disp("Java","Python","KVR","DS") # Function call-4
disp()