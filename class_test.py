# class Parent(object):
# 	def __init__(self, a = 0, b = 1):
# 		print "Zero argument constructor"
# 		self.sum = a + b
# 		print self.sum
# 	def func(self, a):
# 		self.name = a

# 	def display():
# 		print "Name:", self.name

# obj = Parent(1,2)


#!/usr/bin/python

# class Parent:        # define parent class
#    parentAttr = 100
#    def __init__(self):
#       print "Calling parent constructor"

#    def parentMethod(self):
#       print 'Calling parent method'

#    def setAttr(self, attr):
#       Parent.parentAttr = attr

#    def getAttr(self):
#       print "Parent attribute :", Parent.parentAttr

# class Child(Parent): # define child class
#    def __init__(self):
#       print "Calling child constructor"

#    def childMethod(self):
#       print 'Calling child method'

# c = Child()          # instance of child
# c.childMethod()      # child calls its method
# c.parentMethod()     # calls parent's method
# c.setAttr(200)       # again call parent's method
# c.getAttr()          # again call parent's method
# print issubclass(Child,Parent)

# print isinstance(c,Parent)

# print isinstance([1,2,3], tuple)

#!/usr/bin/python

class Parent:        # define parent class
   def myMethod(self):
      print 'Calling parent method'

class Child(Parent): # define child class
   def myMethod(self):
      print 'Calling child method'

c = Child()          # instance of child
c.myMethod()         # child calls overridden method


