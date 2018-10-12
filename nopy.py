n = int(input("Enter no. of rows:"))
s = n-1
for i in range(1,n):
	for k in range(1,s):
		print("")
	for j in range(1,i+1):
		print(" ",j,end=" ")
print("\n")