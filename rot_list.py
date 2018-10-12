def rotate(m,x):
	m[:] = m[-x:] + m[:-x]
m = []
n = int(input("Enter array size:"))
for i in range(n):
	x = int(input())
	m.insert(i,x)
	i = i+1
c = int(input("Which option: 1.Left 2.Right\n"))
if c == 1:
	rotate(m,-1)
	print(m)
if c == 2:
	rotate(m,1)
	print(m)
else:
	print("Enter 1 or 2")