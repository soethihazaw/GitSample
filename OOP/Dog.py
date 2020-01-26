class Dog:

		def __init__(self,name):
			self.name = name
			print('Name', self.name)
		def color(self,color):
			self.color = color
			print('Color', self.name)
		def owner(self,owner):
			self.owner = owner
			print('Dog owner', self.name)
		def age(self,age):
			self.age = age
			print('Dog age is ', self.age)

Dog1=Dog('Aung Net')
Dog1.color('Black')
Dog1.owner('U Kaung')
Dog1.age(7)
