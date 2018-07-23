"""
Collections Module
The collections module is a built-in module that implements specialized container data types providing 
alternatives to Pythons general purpose built-in containers. We've already gone over the basics: dict, list, set, and tuple.

Now we'll learn about the alternatives that the collections module provides.

"""
"""
Counter
Counter is a dict subclass which helps count hash-able objects. Inside of it elements are stored as dictionary keys and 
the counts of the objects are stored as the value.
"""

from collections import Counter

l = [1,2,2,2,2,2,3,3,4,44]
print Counter(l)

print Counter('aabsbsbsbhshhbbsbs')

s = 'How many times does each word show up in this sentence word times each each word'
print Counter(s)
l = s.split()
c = Counter(l)
print c
print c.most_common()

print sum(c.values())                 # total of all counts
                  
print list(c)                         # list unique elements
print set(c)                          # convert to a set
print dict(c)                         # convert to a regular dictionary
print c.items()                       # convert to a list of (elem, cnt) pairs
print Counter(dict(c))    # convert from a list of (elem, cnt) pairs
print c.most_common()[:-1-1:-1]      # n least common elements
c += Counter()                  # remove zero and negative counts
print c
c.clear()     # reset all counts

