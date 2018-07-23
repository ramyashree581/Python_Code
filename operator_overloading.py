#!/usr/bin/python

# class Vector:
#    def __init__(self, a, b):
#       self.a = a
#       self.b = b

#    # def __str__(self):
#    #    return 'Vector (%d, %d)' % (self.a, self.b)
   
#    def __add__(self,other):
#       return Vector(self.a + other.a, self.b + other.b)

# v1 = Vector(2,10)

# v2 = Vector(5,-2)

# print v1 + v2

class Add():

	def __init__(self, a):
		self.a = a
		#print self.a
	def __add__(self, x):
		return self.a+ x.a	
obj = Add(1)	
obj1 = Add(2)
v = obj1 + obj
print v		