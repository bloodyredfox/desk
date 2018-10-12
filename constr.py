class Robot:
	def __init__(self,n,c,w):
		self.name = n
		self.color = c
		self.weight = w
		
	def iself(self):
		print("My name is " + self.name)
		print("Fav color is " + self.color + " \nWeight is " , self.weight)

r1 = Robot("Isha","red",30)
r2 = Robot("Red","black",30)

r1.iself()
r2.iself()