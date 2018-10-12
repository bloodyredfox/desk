def even(n):
	c = 0
	for i in n:
		if i % 2 == 0:
			c += 1
	print(c)
n = [1,32,3,432,12,34]
even(n)