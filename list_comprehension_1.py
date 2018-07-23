# l = input("Enter a value: ")
# l = list[l]
# x = [i*i for i in l]
# print x

l = [{'Age': 25, 'Name': 'Ramya'}, {'Age': 14, 'Name': 'Raksha'}]
inp =
def getAge(inp):
	for item in l:
		if item["Name"] == inp:
			print item["Age"]
			break
		else:
			print "Key not found"	
# inp = input("Enter a name:")
getAge(inp)
