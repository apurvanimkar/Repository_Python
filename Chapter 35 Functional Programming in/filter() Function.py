# Python program to demonstrate working of filter().
lst=[10,20,30,40,50,60,77,101,66]

def high_marks(n):
    if(n>=60):
        return True

r=filter(high_marks,lst)
for i in r:
    print(i)
print(type(r))
