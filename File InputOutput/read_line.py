with open('test.txt', 'r') as f:

	# f_text = f.readline()
	# print(f_text,end='')

	# f_text = f.readline()
	# print(f_text,end='')

	# f_text = f.readline()
	# print(f_text,end='')

	# for f_text in f:  # using for loop to read all line in the file
	# 	print(f_text,end='')

		# f_text=f.read(100) # reading text count eg. how many words in the text file.
		# print(f_text,end='')

		#size_to_read = 100 # reading text count eg. how many words in the text file.
		f_text = f.read(100)
		# # print(f_text,end='')

		while 100 > 0: # Print all Data from the file.
			print(f_text,end='')