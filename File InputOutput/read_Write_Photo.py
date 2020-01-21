with open('cat.jpg', 'rb') as rf:
	with open('cat_copy.png','wb') as wf:

		for line in rf:
			wf.write(line)


			#Write is override function
			#Need Binary format for Photo ......