class Car():

	def __init__(self, name, year):
		self.name = name
		self.year = year

	def drive(self): #instance method
		print "inside Instance method"

	@classmethod
	def drive(cls, name, year):
		print "Inside Class method"
		return cls(name, year-10)

	def display(self):
		print self.name
		print self.year

	@staticmethod
	def drive(name,year):
		print "I am inside static method"

obj = Car("Verna", 2017)
obj.display()	
car1 = Car.drive("Honda", 2018)
car1.display()	
#Car.drive()
Car.drive("Honda", 2001)