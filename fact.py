n = int(input("Find factorial of: "))
f = 1
for i in range(1,n+1):
	f = f * i
	
print("The factorial of %d is",n)
print(f)