l = [1,2,4,5,6,7]

# for i in range(len(l)):
# 	if i in l:
# 		# print i
# 		pass
# 	else:
# 		print "missing :",i 

x = [i for i in range(7) if i in l]
print x

