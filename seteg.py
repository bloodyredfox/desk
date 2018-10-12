n = [ 1,3,4,1,5,3,6,1,2,3,4]
print("Example list\n",n)
set1 = set()
s1 = 0
for i in n:
	set1.add(i)
for i in set1:
	s1 += i
n1 = list()
for i in set1:
	n1.append(i)
s2 = sum(set1)
print("Converting set to list\n",n1)
print("Sum of unique elements = \n",s1,"\nAnd s2 using direct cmmd=\n",s2)
