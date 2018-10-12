def exp(a,n):
	if n==0:
		return 1
	else:
		return (a * exp(a,n-1))
a,n = input("Enter a and the exponant n:\n").split()
a,n=int(a),int(n)
print(a,"raised to",n,"is:",exp(a,n))