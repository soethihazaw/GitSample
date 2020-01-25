#DocString (Documentation Strings)


def print_max(x,y):
	'''	Prints the maximum of two numbers 
		The Two values must be integers.
	'''


	x= int(x)
	y= int(y)

	if x>y :
		print(x, 'is maximum')

	elif x<y:
		print(y,'is maximum')

	else:
		print(x,'and',y,' is equal')

print_max(5,5)

print (print_max.__doc__)