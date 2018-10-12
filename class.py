class Robot:
	def iself(self):
		print("My name is " + self.name)
		print("Fav color is " + self.color + " \nWeight is " ,self.weight)

r1 = Robot()
r1.name = "Isha"
r1.color = "red"
r1.weight = 30

r2 = Robot()
r2.name = "Red"
r2.color = "black"
r2.weight = 30

r1.iself()
r2.iself()