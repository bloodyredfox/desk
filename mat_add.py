n = int(input("Enter matrix size:"))
import numpy as np
m = [[0]*n for i in range(n)]
for i in range(n):
	for j in range(n):
		m[i][j] = int(input())
print(np.matrix(m))

x = int(input("Enter matrix size:"))
y = [[0]*n for i in range(x)]
#if x[i] == y[j]:
for i in range(x):
	for j in range(x):
		y[i][j] = int(input())
print(np.matrix(y))

result = [[m[i][j] + y[i][j]  for j in range
(len(m[0]))] for i in range(len(m))] 
   
for r in result: 
    print(r)
