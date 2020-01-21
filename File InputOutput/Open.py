#"r" - Read

#"a" - Append

#"w" - Write

#"x" - Create

#"t" - Text

#"b" - Binary

#Open & Read File

# f = open('test.txt','r') # R - read

# print(f.name)

# f.close()



with open('test.txt', 'a') as g: #g= open('test.txt','a') # A - Append

	g.write ('This is line number 6'+"\n")

	print(g,end='')