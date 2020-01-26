#Class.py

class Person:
	pass #An empty block

p=Person()
print(p)

#Methods

class Person:
	def say_hi(self):
		print('Hello, how are you?')

p= Person()
p.say_hi()


#__init__method

class Person:
	def __init__(self, name,age,code,gender):
		self.name = name
		self.age = age
		self.code = code
		self.gender = gender

	def say_name(self):
		print ('Hello,my name is', self.name)
	def say_age(self):
		print (' I\'m ',self.age)
	def say_code(self):
		print ('My Code is',self.code)
	def say_gender(self):
		print ('Gender = ',self.gender)



p = Person('Soe Thiha Zaw',26,201078,'Male')
p.say_hi()



# dog= dog('Name')
# dog.color('Black')
# dog.owner('Ko Soe')

# dog.function() - bark
#				 - eat
#				 - sleep
#				 - bite