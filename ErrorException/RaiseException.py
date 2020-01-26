class PasswordException(Exception):
	'''A user-defined exception class.'''
	def __init__(self,length,atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

class UpperLowerException(Exception):
	'''A user-defined exception class.'''
	def __init__(self,upper,lower):
		Exception.__init__(self)
		self.upper = upper
		self.lower = lower
try:
	text = input('Enter something-->')
	if len(text) < 8:
		raise PasswordException(len(text),8)

	elif len(text) > 72:
		raise PasswordException(len(text),72)
		
	elif text == text.lower():
		raise UpperLowerException(text,text.lower())

	elif text == text.upper():
		raise UpperLowerException(text,text.upper())

#Other work can continue as usual here
except EOFError:
	print('Why did you do an EOF on me?')
except PasswordException as exShort:
	print(('PasswordException: The input was' + ' {0} long ,excepted at least {1}').format(exShort.length, exShort.atleast))
except PasswordException as exLong:
	print(('PasswordException: The input was' + ' {0} long ,excepted at least {1}').format(exLong.length, exLong.atleast))
except UpperLowerException as Lowercase:
	print(('UpperLowerException: You need to use atleast one Upper Case letter').format(Lowercase.upper,Lowercase.lower ))
except UpperLowerException as Uppercase:
	print(('UpperLowerException: You need to use atleast one Lower Case letter').format(Uppercase.upper,Uppercase.lower ))
else:
	print('No exception was raised.')

