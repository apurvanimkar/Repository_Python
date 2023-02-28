#Return statement inside loop in a function

def num():
    for number in range(1, 10):
        if (number % 2==0):
            return number
x=num()
print(x)
