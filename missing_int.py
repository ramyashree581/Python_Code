li = [1,2,3,5]
li1 = range(len(li)+2)
print li1
for i in li1:
	if i in li:
		pass 
	else:
		print i	
		