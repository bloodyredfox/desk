m = []
n = int(input("Enter array size:"))
for i in range(n):
	x = int(input())
	m.insert(i,x)
	i = i+1
print("Maximum number in array is:", max(m))
