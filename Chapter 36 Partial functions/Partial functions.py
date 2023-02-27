# Python program to demonstrate working of Partial functions.

#syntax- partial(func,arg1,arg2,....argn)

from functools import partial
def add(n1,n2,n3,n4):
    return n1+n2+n3+n4

add=partial(add,2,3)
print(add(5,10))
