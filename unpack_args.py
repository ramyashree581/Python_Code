def add(*args, **kwargs):
	print *args, **kwargs

l = [1,2,3,4]	
# add(l)# this doesnt work.!!! It says add takes 4 arguments and you have given one
add(*l) # iterates through the list and gives as arguments


# A Python program to demonstrate use
# of packing
 
# This function uses packing to sum
# unknown number of arguments
def mySum(*args):
    sum = 0
    for i in range(0, len(args)):
        sum = sum + args[i]
    return sum
 
# Driver code
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20)) 

