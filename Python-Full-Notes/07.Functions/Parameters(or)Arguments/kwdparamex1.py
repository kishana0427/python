#kwdparamex1.py
def   dispstudinfo(ename,eno,marks,crs,):
	print("{}\t{}\t{}\t{}".format(eno,ename,marks,crs))

#main program
print("Stno\tName\tMarks\tCourse")
print("---------------------------------------------")
dispstudinfo(10,"RS",22.22,"PYTHON") # Possitional Params
dispstudinfo(crs="JAVA",eno=100,ename="JG",marks=11.11) # KWD params
dispstudinfo(marks=22.22,crs="DS",eno=101,ename="Travis") # KWD params
dispstudinfo("TIM",103,crs="Pandas",marks=33.33)
#dispstudinfo(marks=44.44,"TIM",103,crs="Numpy") # positional argument follows																				keyword argument
