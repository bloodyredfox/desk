m = int(input("Enter array size:"))
n = list()
for i in range(m):
	x = int(input())
	n.append(x)
print("Sum of all elements:",sum(n))
print("Average of all elements:",(sum(n))/m)