n = int(input("Enter matrix size:"))
import numpy as np
s = 0
m = [[0]*n for i in range(n)]
for i in range(n):
	for j in range(n):
		m[i][j] = int(input())
print(np.matrix(m))
for i in range(n):
	for j in range(n):
		if i == j:
			s = s + m[i][j]
print("Sum of diagonals:\n",s)