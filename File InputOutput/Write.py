with open('test.txt','r') as rf:
	with open('testCopy.txt','w') as wf:

		for line in rf:
			wf.write(line)

