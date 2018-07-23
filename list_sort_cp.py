# data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
# new_list = []

# while data_list:
#     minimum = data_list[0]  # arbitrary number in list 
#     for x in data_list: 
#         if x < minimum:
#             minimum = x
#     new_list.append(minimum)
#     data_list.remove(minimum)    

# print new_list


li = [1,2,3,4,5,'Ramya',6,7,8,"Yelahnka",0.57]
li_int = []
li_str = []
li_float = []

# for each in li:
# 	##print type(each)
# 	if type(each) == str:
# 		li_str.append(each)

# 	elif type(each)	== int:
# 		li_int.append(each)
# 	else:
# 		li_float.append(each)	

# print li_str, li_float, li_int
	
for each in li:
	if isinstance(each, str):
		li_str.append(each)
	elif isinstance(each, int):
		li_int.append(each)
	else:
		li_float.append(each)
print li_int, li_float, li_str

