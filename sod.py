def sum(n):
	r,c = 0,0
	while(n):
		r,n,c = r + n % 10, n //10, c + 1
	return (r,c)  
n = int(input("Enter a no. :"))
print("Sum and Count:",sum(n))