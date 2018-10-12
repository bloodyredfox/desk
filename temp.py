n = 0
n = int(input("C or F; enter 1 or 2\n"))
if n == 2:
	c = float(input("Enter temperature in celcius: "))
	print("Temp in F is :",float((c*1.8)+32))
elif n == 1:
	f = float(input("Enter temperature in fahrenheit: "))
	print("Temp in C is :",float(f-32)*0.56)
else:
	print("... 1 or 2")