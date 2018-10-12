a = set()
print(a)
a.add(1)
print(a)

n = [ 1,2,2,3,4,4,4,5,6,6,6,6,6,7,8,8,8,8,8,8,8]
print("Example list\n",n)
set1 = set()
for i in n:
	set1.add(i)
print("Converting to set to remove duplicates\n",set1)

n1 = list()
for i in set1:
	n1.append(i)
print("Converting set to list\n",n1)

