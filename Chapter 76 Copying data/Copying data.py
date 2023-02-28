#Copying data

#Copy a dictionary:=

original = {1:'one', 2:'two'}
new = original.copy()

print('Orignal: ', original)
print('New: ', new)
print("---------------------------------")

#Performing a shallow copy(modifiction cannt afect orignal)
ori = {
    "Hello": 56,
    "at" : 23 ,
    "test" : 43,
    "this" : 43,
    "who" : [56, 34, 44]
    }
# create a Shallow copy  the original dictionary
newDict = ori.copy()
print(newDict)
newDict["at"] = 200
print(newDict)
print(ori)

