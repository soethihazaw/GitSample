class ShortInputException(Exception):
	'''A user-defined exception class.'''
	def __init__(self,length,atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

class LongInputException(Exception):
	'''A user-defined exception class.'''
	def __init__(self,length,atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

try:
	text = input('Enter something-->')
	if len(text) < 3:
		raise ShortInputException(len(text),3)
	elif len(text) > 10:
		raise LongInputException(len(text),10)

	#Other work can continue as usual here

except EOFError:
	print('Why did you do an EOF on me?')

except ShortInputException as exShort:
	print(('ShortInputException: The input was' + ' {0} long ,excepted at least {1}').format(exShort.length, exShort.atleast))

except LongInputException as exLong:
	print(('LongInputException: The input was' + ' {0} long ,excepted at least {1}').format(exLong.length, exLong.atleast))

else:
	print('No exception was raised.')

