import  math
m,s,v = [],0,0
n = int(input("Enter array size:"))
for i in range(n):
	x = int(input("Enter value:"))
	m.insert(i,x)
	i = i+1
	s = s + x
a = s/n
print("sum:\n",s)
for i in range(len(m)):
	v = v + math.pow((a - m[i]),2)
	v = v/n
print("Var:\n",v)
d = math.sqrt(v)
print("STD:\n",d)