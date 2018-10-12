list = [9,6,5,4,4,4,-1,-1,-3,-4]
t,i = 0,0
while i < len(list):
	#print(list[i])
	if list[i]<=0:
		t += list[i]
		i += 1
	else:
		i += 1
print("Total:",t)