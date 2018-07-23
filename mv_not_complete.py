stringToMatch = 'is not complete'
matchedLine = ''

#get line
with open('/mqm/log/Importerd/2018/04-April/29-Sunday.log', 'r') as file:
	for line in file:
		if stringToMatch in line:
			matchedLine = line
			break

#and write it to the file
with open('/mqm/data/import/mv_not_complete.log', 'w') as file:
	file.write(matchedLine)
import os
import subprocess
import re
# os.getcwd()
# os.listdir("/mqm/data/import/transferQSMC_a0")
res = re.search("/mqm/data/import/transferQSMC_[A-Z a-z 0-9]*/QSMC_[A-Z]*_[0-9]*-[0-9]*", matchline)
res = res.group()
cmd = "mv "+ res + "/mqm/data/import/bad_transferQSMC/"
subprocess.call(cmd, shell=True)



# stringToMatch = 'is not complete'
# matchedLine = ''

# #get line
# with open('/mqm/log/Importerd/2018/04-April/29-Sunday.log', 'r') as file:
#         for line in file:
#                 if stringToMatch in line:
#                         matchedLine = line
#                         break
# print matchedLine
# # #and write it to the file
# with open('/mqm/data/import/mv_not_complete.log', 'w') as file==[p]
#         file.write(matchedLine)
# import subprocess
# import re
# # os.getcwd()
# # os.listdir("/mqm/data/import/transferQSMC_a0")
# res = re.search("/mqm/data/import/transferQSMC_[A-Z a-z 0-9]*/QSMC_[A-Z]*_[0-9]*-[0-9]*", matchedLine)
# res = res.group()
# cmd = "mv "+ res + "/mqm/data/import/bad_transferQSMC/"
# subprocess.call(cmd, shell=True)