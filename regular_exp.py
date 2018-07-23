s = 'Raksha6163884116yelahanka560065'
import re
regex = re.compile('(?P<Name>\w+) (?P<Phone>\w+) (?P<Address>\w+)')
st =  re.search(regex, s)
print st
# print s.isalnum()
# print s.isalpha()
# l = []
# for item in s:
# 	# if item.isalpha()
# 	print item
