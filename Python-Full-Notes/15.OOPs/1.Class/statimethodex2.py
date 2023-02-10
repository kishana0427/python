#statimethodex2.py
#This program demonstartes the static method and cal any aop
class ArithmeticOperations:
	def   readvalues(self):
		self.a, self.b=float(input("Enter First Value:")), float(input("Enter Second Value:"))
		self.op=input("Enter the arithmetic operator symbol:")

class Calculator:
	@staticmethod
	def   operations(obj):
		match obj.op:
			case "+":
				print("sum({},{})={}".format(obj.a,obj.b,obj.a+obj.b))
			case "-":
				print("sub({},{})={}".format(obj.a,obj.b,obj.a-obj.b))
			case "*":
				print("mul({},{})={}".format(obj.a,obj.b,obj.a*obj.b))
			case "/":
				print("div({},{})={}".format(obj.a,obj.b,obj.a/obj.b))
			case "//":
				print("floor div({},{})={}".format(obj.a,obj.b,obj.a//obj.b))
			case "%":
				print("mod({},{})={}".format(obj.a,obj.b,obj.a%obj.b))
			case "**":
				print("pow({},{})={}".format(obj.a,obj.b,obj.a**obj.b))
			case _ :
				print("{} is not a Arithmetic Operator Symbol:".format(obj.op))
	
	
#main program 
ao=ArithmeticOperations()
ao.readvalues()  # {'a': 12.0, 'b': 34.0, 'op': '+'}
Calculator.operations(ao)