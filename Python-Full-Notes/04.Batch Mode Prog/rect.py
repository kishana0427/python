#Program for cal area and perimeter of Rectangle
#Area of Rect = length * breadth
#Perimter= 2(length+breadth)
#rect.py
l=float(input("Enter Length:"))
b=float(input("Enter Breadth:"))
#cal area and peri
ar=l*b
pr=2*(l+b)
# diplay the result
print("-"*40)
print("Length={}".format(l))
print("Breadth={}".format(b))
print("Area of Rect={}".format(ar))
print("Peri of Rect={}".format(pr))
print("#"*50)