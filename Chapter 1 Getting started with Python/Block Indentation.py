

def my_function():   # This is a function definition. Note the colon (:)
    a = 2            # This line belongs to the function because it's indented
    return a         # This line also belongs to the same function
print(my_function()) # This line is OUTSIDE the function block

a,b = 10,20
if a > b:             # If block starts here
    print(a)              # This is part of the if block
else:                 # else must be at the same level as if
    print(b)              # This line is part of the else block

#Blocks that contain exactly one single-line statement
if a > b: print(a)
else: print(b)
