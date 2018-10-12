def prime(n):
	c = 0
	for i in range(1,n+1):
		if n % i == 0:
			c = c + 1
	if c == 2:
		return 0
	else:
		return 1
n = int(input("Enter prime range:"))
for i in range(1,n+1):
	r = prime(i)
	if r == 0:
		print(i)

