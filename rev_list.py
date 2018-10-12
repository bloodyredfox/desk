m = []
n = int(input("Enter array size:"))
for i in range(n):
	x = int(input())
	m.insert(i,x)
	i = i+1
x = m
print("Original list:\n",x)
m.reverse()
print(m)
