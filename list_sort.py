"""
python: order a list of numbers without built-in sort, min, max function

"""

# l = [-5, -23, 5, 0, 23, -6, 23, 67]
# # l.sort(reverse = True)
# # print l
# l_new = []
# data = l
# list_length =len(data)
# print list_length

# while l:
# 	list_length =len(data)
# 	min_val = l[0]
# 	for item in range(list_length):
# 		if l[item] < min_val:
# 			min_val = l[item]

# 	l_new.append(min_val)

# 	l.remove(min_val)
# print l_new
# print l_new[-2]
# print l_new[1]

# for x in [1,2,3] : 
# 	print(x)

s = "yelahanka new town"
count = 0
#for each in range(len(s)):

# if "e" in s and count == 2:
# 	print s[]
	
# elif "e" in s:
# 	count += 1
# else:
# 	pass

count = 0
for k,v in enumerate(s):
	# print k, v
	if "e" == v:
		count = count +1

	else:
		pass
	if count == 2:
		print "k:", k



# print s
# print (s.find('t'))
# print "occurence of e"
# print (s.find('e'))
# print s.index('e')

# for i in range (len(s)):
# 	if 'e' in  s:
# 		print s.index('e')
# 		count = s.index('e')
		




"""
1st iteration:
	-5
	min_val = -5
	item 0 
"""

#for i in range(list_length):
# 	for item in l:
# 		if item < x:
# 			i = i+1
# 		else:
# 			 l_new.append(x)	
# print l_new		
