class Length:
	def __init__(self,c,m):
		self.c = c
		self.m = m

	def __str__(self):
		return("Length (%d cm,%d mm)" %(self.c,self.m))

	def __add__(self,other):
		return (Length(self.c+other.c, self.m+other.m))

l1 = Length(2,3)
l2 = Length(3,5)
print l1+l2

##*****************MULTIPLICATION******************##

class Multi:
	def __init__(self, a , b):
		self.a = a
		self.b = b
	def __mul__(self,other):
		return(Multi(self.a*other.a, self.b*other.b))

	def __str__(self):
		return("Multi (%d ,%d )" %(self.a,self.b))

l1 = Multi(2,3)	
l2 = Multi(4,5)
print l1*l2
