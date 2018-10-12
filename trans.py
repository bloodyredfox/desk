m = [[1,2,3],[4,5,6],[7,8,9]]
for n in m:
	print(n)
t = [[m[j][i] for j in range(len(m))] for i  in range(len(m[0]))]
print("\n")
for n in t:
	print(n)
	
	
