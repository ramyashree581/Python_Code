"""
all is a python built-in function which checks all the itearable of an iterator are True


all() and any() are built-in functions in Python that allow us to conveniently check for boolean matching in an iterable. 
all() will return True if all elements in an iterable are True. It is the same as this function code:



any() will return True if any of the elements in the iterable are True. It is equivalent to the following function code:

Let's see a few examples of these functions. They should be fairly straightforward:
"""

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

lst = [True,False,False,False]  
print all(lst)
print any(lst)