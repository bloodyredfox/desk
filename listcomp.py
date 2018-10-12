a = [1,3,5,7,9]
print("A=\n",a)
b1 = []
for i in a:
	b1.append(i * 2)
print("B1 using append=\n",b1)
b2 = [i*2 for i in a]
print("B2 using list comphrension=\n",b2)
d1 = [i**2 for i in range(1,11)]
print("D using LC=\n",d1)
d2 = [i**2 for i in range(10,0,-1)]
print("D2=\n",d2)