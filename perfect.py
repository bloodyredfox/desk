n = int(input("Enter a number:"))
s = 0
for i in range(1,n):
	if n%i == 0:
		s = s+i
if n == s:
	print("Perfect")
else:
	print("Not Perfect")