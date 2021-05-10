for s in input():
	print(s*sum([int(x) for x in str(ord(s))]))