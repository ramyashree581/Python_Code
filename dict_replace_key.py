
l = [{"Name": "Ramya", "DEPT": 1}, {"Name": "Raksha", "DEPT": 2}, {"Name":"Rashmi","DEPT":3}]
# for item in l:
# 	if item.keys() == "Name":
# 		print 
# res = l[0].keys()
# res[1] = "Fullname"
# print res

res = l[0]
res["Fullname"] = res["Name"]
print res
del res["Name"]
print res
print