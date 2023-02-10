#matchcaseex2.py
wkno=int(input("Enter Week Number:"))
match wkno:
	case 1|2|3|4|5|6:
			print("Its working")
	case 7:
			print("Its SUNDAY_holy Day and Joy day")
	case _:
			print("Its not a week number--learn weeks  ")
print("Program over")
	
	
			