d = {'name':'Ramya'}
d["fullname"] = d.get("name")
print d
del d["name"] #to delete old entry
print d
################################
d = {'name':'Ramya'}
import json
res = json.dumps(d)
print res
print type(res)
print res.replace('name', 'fullname')
d = json.loads(res)
print d


print range(10)