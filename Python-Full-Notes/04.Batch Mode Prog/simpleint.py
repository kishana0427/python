#program for simple interest and total amount to pay
#simpleint.py
p=float(input("Enter Principle Amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate of Interest:"))
#calcuate si
si=(p*t*r)/100
#calculate total amount to pay
totamt=p+si
print("----------------------------------------------")
print("\tSimple Intrest results")
print("----------------------------------------------")
print("\tprinciple Amount={}".format(p))
print("\tTime={}".format(t))
print("\tRate of Interest={}".format(r))
print("----------------------------------------------")
print("\tSimple Interest on Princple={}".format(si))
print("\tTotal Amount={}".format(totamt))
print("----------------------------------------------")