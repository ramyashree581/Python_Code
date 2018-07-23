# '''
# #################IndexError#############################
# '''
# l = [1,2,3]
# try:
# 	print l[4]
# 	l.append(5)

# except IndexError as err:
# 	print "Exception has occured: ", str(err)

# finally:
# 	l.append(5)
# print l
# '''
# #################KeyError#############################
# '''
# di = {"name": "Ramya"}
# try: 
# 	di["dept"]
# except KeyError as err:
# 	print "Exception has occured: ",str(err) 
# import sys
# '''
# ##################StopIteration############################
# '''
# try:
# 	   z = [5, 9, 7]
# 	   i = iter(z)
# 	   print i
# 	   print i.next()
# 	   print i.next()
# 	   print i.next()
# 	   print i.next()
# except StopIteration as err:
# 	print "Exception: ", sys.exc_type
# '''
# ################Exception##############################
# '''
# try:
# 	l = [1,2,3,4]
# 	print l[5]
# except Exception:
# 	print "err"

# '''
# #################EOFError#############################
# '''
# import sys
# a = 1
# b = 2
# c = 3
# if b == 3:
# 	c = c+1
# else:
# 	print a, b, c
# 	# sys.exit()
# try:
# 	x = input("Enter an val:")
# 	print x
# except EOFError as err:
#      print "Exception due to no input:", str(err)
# '''
# ###############Exception###############################
# '''

# try:
#     check = input ("would you like to continue?:")
# except Exception:
#     print "Error: EOF or empty input!"
#     check = ""

# finally:
# 	print check
# '''
# ################KeyboardInterrupt##############################
# '''


# try:
# 	check = input("something")
# except KeyboardInterrupt:
# 	print "caught"
# '''
# ####################ImportError##########################
# '''

# try:
# 	import text.py
# 	import os
# 	pwd = os.chdir("/tmp/")
# 	print pwd

# except ImportError:
# 	print "Caught"

'''
######################SyntaxError########################
'''
try:
	print eval('five times three')

except SyntaxError, err:
	print 'Syntax error %s (%s-%s): %s' % \
	 (err.filename, err.lineno, err.offset, err.text)
	 print err

	