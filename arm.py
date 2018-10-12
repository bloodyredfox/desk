n = int(input("Enter a number:"))
t,r = n,0
while t != 0:
	r,t = r + ((t%10)**(len(str(n)))),t//10
print(r)
if n == r:
	print("Armstrong")
else:
	print("Not Armstrong")