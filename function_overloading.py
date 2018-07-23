
class Addition(object):

	def add(self,*args, **kwargs):
		# for arg in args:
		# 	print arg
		for arg in args:
			print arg
		for item in kwargs:
			print item
		#self.sum = a+b+c
		#print self.sum
		pass

	# def add(self,a,b,c):
	# 	self.sum = a+b+c
	# 	print self.sum

obj = Addition()
#obj.add(2,3)
obj.add(2,3,4,{"name":"ramya"})

"""
What is function overloading?
Same function having different in number of arguments, order of arguments and type of arguments
"""

'''
function overloading 
'''
class A():
	def add(self, a=0):
		self.a = a+1
		print self.a 

obj = A()	
obj.add(1)	

