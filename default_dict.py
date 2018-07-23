"""
A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory.

"""


from collections import defaultdict

# d  = defaultdict(object)
# d["key1"]  = 1
# print d.get("key1")
# print d.get("key2")
d = {"key1":1}
print d.get("key2")

"""
OrderedDict
An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.
"""

print 'Normal dictionary:'

d = {}

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print k, v

print "#######################"
#####################################

from collections import OrderedDict

d = OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print k, v

"""
A regular dict looks at its contents when testing for equality. An OrderedDict also considers the order the items were added.
"""
print 'Dictionaries are equal? '

d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2


print "-----------------"


print 'Dictionaries are equal? '

d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'


d2 = collections.OrderedDict()

d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2