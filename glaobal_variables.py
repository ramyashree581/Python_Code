# # This function has a variable with
# # name same as s.
# def f(): 
#     s = "Me too."
#     print s 
 
# # Global scope
# s = "I love Geeksforgeeks"
# f()
# print s

global s
s = 'Keep calm and work hard'
print s
def f():
	s = 'same here'
	print s
print s

f()	




