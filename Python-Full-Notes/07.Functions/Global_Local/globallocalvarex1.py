#globallocalvarex1.py
lang="PYTHON"  # here the variable lang is called Global Variable.
def  learnML():
	sub1="ML"  # here sub1 is called Local Variable
	print("\nBy Using '{}' we develop '{}' applications".format(lang,sub1))
	#print(sub2,sub3) we can't access sub2 and sub3 of other functions.
def  learnDL():
	sub2="DL"  # here sub2 is called Local Variable
	print("\nBy Using '{}' we develop '{}' applications".format(lang,sub2))
	#print(sub1,sub3) we can't access sub1 and sub3 of other functions.
def  learnIOT():
	sub3="IOT"  # here sub3 is called Local Variable
	print("\nBy Using '{}' we develop '{}' applications".format(lang,sub3))
	#print(sub1,sub2) we can't access sub1 and sub2 of other functions.


#main prog
learnML()
learnDL()
learnIOT()