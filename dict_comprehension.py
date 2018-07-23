#print squares of these numbers
di = {0:0, 1:1, 2:2, 3:3, 4:4}
for i in di:
	print i*i

squares = {x:x*x for x in range(5)} #dict comprehension with range
print squares
squares = {x:x*x for x in di} # dict comprehension with dict
print squares

'''
print ODD squares
'''

odd_squares = {x:x*x for x in range(11) if x%2==1}
print odd_squares

odd_squares = {x:x*x for x in di if x%2 == 1} 
print odd_squares

'''
print only the vlaues of the keys
'''

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])


keys = {'a', 'e', 'i', 'o', 'u' }

vowels = dict.fromkeys(keys)
print(vowels)
