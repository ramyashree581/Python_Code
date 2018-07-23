import json

li1 = [1,2,3,4]
li2 = [5,6,7,8]
#li1.append(li2)
#print li1 
#li1.extend(li2)
#print "li.extend :", li1

"""
In Append functionality the appended list is added as it is.
But in extend method it iterates the second list and adds each element
"""

li1.append("Ramya")
print li1
li1.insert(4, "Hari")
print li1

li1.pop()
li1
print li1

del li1[4]
print li1

li1.remove(4)
print li1

"""
In pop, del method, you need to give index but in remove method you need to supply the element
"""
# li = [1,2,3,4]
# li1 = [2,3,4,5]
# li.append(li1)
# print "li.append :", li
# # set(li1)
# # print li1


# # li2 = li[0:4]
# # li3 = li[4:]
# # print li1
# print str(li)

