# class Car(object): #New design
# 	count = 0 # class variable  

# 	'''
# 	A constructor will initialize the datamember of the class
# 	Constructor is called when object is created
# 	variables used inside the function is called  instance variables. self.name and self.age are instance variables 
# 	'''
# 	def __init__ (self, name, age): #constructor, this is 0 arguments constructor if it doesnt cotain any args
# 		self.name = name #initializing data member using self
# 		self.age = age #Instance variable

# 	def displayNameAge(self):
# 		print "Name is: ", self.name
# 		print "Age is:		", self.age

'''
Create a class, 
'''
# class A(object):
# 	count = 0
# 	def display(self):
# 		self.count = A.count+1
# 		return self.count

# class B(A):
# 	#print "Count of B is: ", A.count	
# 	obj = A()
# 	res = obj.display()
# 	print res
# obj = Car("ramya", 25)
# obj.displayNameAge()
# print Car.count


# class A():
# 	def display(self):
# 		self.a = 1
# 		return self.a

# class B(A):
# 	obj = A()
# 	res = obj.display()
# 	print res


# obj = A()
# res = obj.display()	
# print res



# class A():
# 	def display(self):
# 		print "I am in A"

# class B():
# 	def display(self):
# 		print "I am in B"`

# class C(B):
# 	#def display(self):
# 	print "I am in C"
	


# obj = C()
# obj.display()



class Employee(object):
	
	def __init__(self, name, age):
		self.name = name
		self.age = age

obj = Employee('Ramya',3)
obj1 = Employee('Hari', 8)



print hasattr(obj,'age') # check if an attribue(data member) is present inside the object. Returns True if present
print getattr(obj,'name') # returns the value of the attribute(data member)
print getattr(obj1,'name')

setattr(obj, 'name', 'Rashmi') #Set the value of attribute to some other value, RETURNS  none 
print getattr(obj,'name') # get the value after it is set

delattr(obj,'age') # Deletes the attribute of an object , Returns None












