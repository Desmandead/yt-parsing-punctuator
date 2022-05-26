with open('input.txt') as f:
	contents = f.read()
	contents = contents.replace("\r"," ")
	contents = contents.replace("\n"," ")
	print(contents)