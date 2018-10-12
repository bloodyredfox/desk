m = []
n = int(input("Enter array size:"))
for i in range(n):
	x = int(input())
	m.insert(i,x)
	i = i+1
k = int(input("Enter element to be found:"))
if k in m:
	print("Element found")
else:
	print("Element not found")