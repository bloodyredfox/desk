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

class Person():
	def __init__(self,n,p,i):
		self.name = n
		self.personality = p 
		self.sitting = i 
	def sit(self):
		self.sitting = True
	def stand(self):
		self.sitting = False
	def p(self):
		print("Name is " + self.name + " and personality is "+ self.personality)
p1 = Person("Isha","silent",False)
p2 = Person("Red","talkative",True)
p1.robot = r2
p2.robot = r1

p1.p()
p2.robot.iself()
	
	
	