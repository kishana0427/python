#program for swapping any values with multi line assignment
#swap.py   
a=input("Enter Value a:")
b=input("Enter Value b:")
print("="*40)
print("Orginal Val of a={}".format(a))
print("Orginal Val of b={}".format(b))
print("="*40)
#swaping logic
a,b=b,a
print("Swapped Val of a={}".format(a))
print("Swapped Val of b={}".format(b))
print("="*40)