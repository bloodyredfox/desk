import math
def semi(a):
	s = 0
	for i in range(2, int(math.sqrt(a)) + 1):
		while a % i ==0:
			a /= i
			s += 1
		if s >= 2:
			break
		if ( a > 1):
			s += 1
		return s == 2
def check(a):
	if semi(a) == True:
		print("Yes")
	else:
		print("No")
	

#m = []
n = int(input("Enter no. of testcases:\n"))
for i in range(n):
	x = int(input())
	check(x)
	#m.insert(i,x)
	#i = i+1
#for i in m:

#check(m)
	


	
	
	