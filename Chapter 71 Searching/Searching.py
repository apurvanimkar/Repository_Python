#Searching for an element

#List
alist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(5 in alist) # True
print(10 in alist) # False

#Tuple
atuple = ('0', '1', '2', '3', '4')
print(4 in atuple) 
print('4' in atuple)

#String
astring = 'i am a string'
print('a' in astring) # T
print('am' in astring) # T
print('I' in astring)# F

#Set
aset = {(10, 10), (20, 20), (30, 30)}
print((10, 10) in aset) #T
print(10 in aset) #F
