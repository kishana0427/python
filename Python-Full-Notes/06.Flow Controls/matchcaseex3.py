#matchcaseex3.py
wkno=input("Enter Week Name:")
match wkno[0:3].lower():
	case "mon"|"tue"|"wed"|"thu"|"fri":
			print("{} is working".format(wkno))
	case "sun":
			print("{} is Holiday".format(wkno))
	case "sat":
			print("{} is week end".format(wkno))
	case _:
			print("Its not a week number--learn weeks  ")
print("Program over")
	
	
			