l = [{"name": "Ramya","dept":"Student"},{"name":"Hari","dept": "Teacher"}]
# print l[0]["dept"]
# val = raw_input("input :",)
# print "input: ", val
# for val in l.keys():
# 	if val == "Ramya" :
# 		print ["dept"]

for each_dict in l:
	#print each_dict
	if each_dict["name"] == "Hari":
		print each_dict["dept"]
		break
