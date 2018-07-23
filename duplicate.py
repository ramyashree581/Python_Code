l = [1,2,2,2,3,3,4,5,6,7,77,8] # I need a list where only unique elements should be present without using any built function
print set(l)
l_new = []
for item in l:
	if item in l_new:
		pass
	else:
		l_new.append(item)
print l_new		

