for item in range(10):
	print item

x = [item for item in range(10)]
print 

print "*******************"
squares = []

for x in range(10):
    squares.append(x**2)
print squares  

squares = [i**2 for i in range(10)]
print squares

"""
multiply every part of the list by 3
"""

li = [3,4,5,6]
multiplied = [item*3 for item in li]
print multiplied

"""
convert lowercase to uper case
"""
strings = "ramya"
letters = [i.upper() for i in strings]
print letters

"""
extract numbers from strings
"""
string = "Hey Ramya 7653623"
x = [i for i in string if i.isdigit()]
x1 = [i for i in string if i.isalpha()]
print x, x1


"""
if number is less than 45 add 5 else add 10
"""
l = [22, 13, 45, 50, 98, 69, 43, 44, 1]

for item in l:
	if item<45:
		print "item less than 45 :", item
		item + 5 
		print item
	else:
		print "item greatere than 45:", item
		item + 10
		print item

x = [x+5 if x>45 else x+10 for x in l ]	
print x	










