#defaultparamex1.py
def  dispstudinfo(sno,sname,marks,crs="PYTHON",cnt="INDIA"):
	print("{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))

#main program
print("------------------------------------------")
print("Stno\tName\tMarks\tCourse\tCountry")
print("------------------------------------------")
dispstudinfo(10,"Shital",66.66)
dispstudinfo(20,"Prassh",56.66)
dispstudinfo(30,"Srini",76.66)
dispstudinfo(40,"Manss",56.66)
dispstudinfo(50,"Manish",66.66)
dispstudinfo(60,"Ajay",56.66)
dispstudinfo(70,"nani",76.66,"JAVA")
dispstudinfo(80,"Adarsh",86.66,"DS","USA")
dispstudinfo(90,"Arjun",56.66)
dispstudinfo(15,"Vin-Chan",44.44,"PYTHan-Java")
dispstudinfo(16,"Kawale",44.44,"")
print("------------------------------------------")