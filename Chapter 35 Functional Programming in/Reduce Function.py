# Python program to demonstrate working of reduce().
import functools
def fun(a,b):
    return a+b

lst=[1,2,3,4,5]

res=functools.reduce(fun,lst)
print(res)
