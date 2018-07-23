# import re
# line = "My name is Ramyashree    M R"
# matchObj = re.match( r'(.*) is (.*?) .*', line, re.M|re.I)
# print matchObj.group(2)


import re
# var1 = "https://intolligent.com/WorkFlow-12345678910abAFFAFcdefg/glace"
# m = re.search(r'WorkFlow-[0-9a-zA-Z]+', var1)
# # matched = re.search('(*)', var1)- .
# print m.group()
var2 = 'RAMYAshreeMR'
nameObj = re.search(r'[A-Z]+', var2)
print nameObj.group()

# # x = "12345"
# # matched = re.match('(\d{2,3})', x)
# # print matched.group()


# # var3 = "Ramyashree is awesome"
# # maches = re.match('.*?', var3)
# # print maches.group(0)

# import re
# var3 = "Ramyashree is awesome"
# res = re.sub('awesome','super',var3)
# print res

# import re

# line = "Manchenahalli Rajgoapl Ramyashree";

# searchObj = re.match('(Ramyas[a-z]+)', line)

# print searchObj.group()