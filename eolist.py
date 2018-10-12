m = []
n = int(input("Enter array size:"))
for i in range(n):
	x = int(input())
	m.insert(i,x)
	i = i + 1
for index in range(len(m)):
	if m[index]%2==0:
		print("Even:",m[index])
	else:
		print("Odd:",m[index])