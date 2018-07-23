a = 1
b = (1,2,3)
print id(a)
print id(b)
a=b   #shallow copy, copies memry loc, a & b will be pointing to same loc
print id(a)
print id(b)

a = b[::] #deep copy, copies only value not the memory. Works for mutable objects
print id(a)
print id(b)

# >>> b = [2,3,5,6]
# >>> id(b)
# 4445651024
# >>> c = [4,5,6,7]
# >>> id(c)
# 4445687608
# >>> b = c[::]
# >>> id(c)
# 4445687608
# >>> id(b)
# 4445824424