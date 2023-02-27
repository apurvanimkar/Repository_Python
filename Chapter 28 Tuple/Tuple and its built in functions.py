#Tuple
#it is common to enclose tuples in parentheses
t = ('a', 'b', 'c', 'd', 'e')
t1 = 'a', 'b', 'c', 'd', 'e'
print(t1)
#Type checcking:-
t2 = ('a',)
x=type(t)
print(x)

#Built-in Tuple Functions:-
#1)Tuple Length
t1=(2,3,4,10,23)
len(t1)

#Max
x1=max(t1)
print(x1)

#Min
x1=min(t1)
print(x1)

#Convert a list into tuple
list = [1,2,3,4,5]
tuple(list)
print(tuple)

#Tuple concatenation
t1=('A','B')
t2=('X','Y','Z')
x=t1 + t2
print(x)
