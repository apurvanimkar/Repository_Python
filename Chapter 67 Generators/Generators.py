#Generators()-return sequence of values ,
#we use yield() to return value from func into generator obj.
#next() Function-retirved elements by elements from generator obj

def disp(a,b):
    yield a
    yield b

r=disp(10,30)
print(r)
print(type(r))

#using next()
print(next(r))
print(next(r))

print("----------")
#2nd Ex:
def show(a,b):
    while(a<=b):
        yield a
        a=a+1

r=show(1,5)
print(r)
print(type(r))
print(next(r))
print(next(r))
print(next(r))
#or
for i in r:
    print(i)
