l1 = [1,2,3,4]
l2 = [3,4,5,6]
print l1.append(l2) #[1, 2, 3, 4, [3, 4, 5, 6]] appends the list as it is to other list.
'''
memory location of li and l2 will be different. after it appends memory location of 2nd list is appended to memory location of first list
ideally thre will be 2 memory locations of 1st list and 2nd 

''' 
print l1
l1.extend(l2) #[1, 2, 3, 4, 3, 4, 5, 6] will extend the file list to accomodate the 2nd list . Iterates the second list and adds the list the 1st list 
'''
takes the 2nd list and extends the first list in same memory as of first list
'''
print l1
l3 = l1 +l2 # [1, 2, 3, 4, 3, 4, 5, 6] concatenation of 2 lists, creates  a new list 
print l3

l3 = set(l1) - set(l2) #difference of 2 lists , set([1, 2]) 
print l3

