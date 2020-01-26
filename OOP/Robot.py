#Class And Object Variables

class Robot:
		""" Represents a robot,with a name."""

		population = 0

		def __init__(self,name):
			""" Initializes the data."""

			self.name = name
			print("(Initializing{})".format(self.name))

			Robot.population +=1

		def die(self):
			""" I am dying """

			print("{} is being destroyed!".format(self.name))

			Robot.population -=1

			if Robot.population ==0:
				print("{} was the last one.".format(self.name))
			else:
				print("There are still {:d} robots working.".format(Robot.population))

		def say_hi(self):
			""" Greeting by the robot.
			Yeah, they an do that."""

			print("Greeting, my sisters call me {}.".format(self.name))

		@classmethod
		def how_many(cls):
				"""Ritnts the current population."""
				print("We have {:d} robots.".format(cls.population))
