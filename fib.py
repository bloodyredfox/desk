n1,n2=0,1
w = int(input("Enter range: "))
for i in range(0,w):
	n = n1 + n2
	n1 = n2
	n2 = n
	print(n1)
	
x,y,i=0,1,1	
w = int(input("Enter range again: "))
while(i <= w):
	print(y)
	x,y = y,y+x
	i = i+1