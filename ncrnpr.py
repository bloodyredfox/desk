def fact(n):
	if n == 0:
		return 1
	else:
		return (n * fact(n-1))
n,r = input("Enter 2 numbers:\n").split()
n,r=int(n),int(r)
npr = fact(n)/fact(n-r)
ncr = npr/(fact(r))
print(f'NPR:{npr} and NCR:{ncr}')
	