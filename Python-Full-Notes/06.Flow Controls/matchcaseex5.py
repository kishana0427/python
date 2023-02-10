#matchcaseex5.py
d={"MONDAY":1,
      "TUESDAY":2,
      "WEDNESSDAY":3,
       "THURSDAY":4,
      "FRIDAY":5,
      "SATURDAY":6,
	  "SUNDAY":7}
wkn=input("Enter Week Name:")
if (d.get(wkn.upper())==None):
	print("Invalid Week Name:")
else:
	match wkn[0:3].lower():
		case "mon"|"tue"|"wed"|"thu"|"fri":
				print("{} is working".format(wkn))
		case "sun":
				print("{} is Holiday".format(wkn))
		case "sat":
				print("{} is week end".format(wkn))
