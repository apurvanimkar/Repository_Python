
class ExampleClass:          #Every function belonging to a class must be indented equall
    def __init__(self):
        name = "example"
        
    def someFunction(self, a):#Notice everything belonging to a function must be indented
        if a > 5:
            return True
        else:
            return False

#If a function is not indented to the same level it will not be considers as part of the parent class
def separateFunction(b):
    for i in b:            #Loops are also indented and nested conditions start a new indentation
        if i == 1:
            return True
    return False

separateFunction([2,3,5,6,1])

#Second Example:---

a = 7
if a > 5:
    print ("foo")
else:
    print("bar")
print("done")
