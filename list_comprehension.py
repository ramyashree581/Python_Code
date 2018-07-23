

mylist = []
for i in 'Ramya':
	mylist.append(i)
print mylist


x = [i**3 for i in {3,1,2}]
print x

x= [i for i in range(8) if i%2 == 0]
print x

x = [i for i in range(8) if i%2==0 if i%3==0]
print x

x = ["Even" if i%2==0 else "Odd" for i in range(8)]
print x
print "############################################"

l = [2,3,4,4,5,7]
li =[]
x = [li.append(i) if i >2 else l.pop(i) for i in  l]
print l
print li


# for i in l:
# 	if i>2:
# 		li.append(i)
# print li		








