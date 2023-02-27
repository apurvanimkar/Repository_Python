#list of keyword in python
import keyword
print(keyword.kwlist)
# Integer
a = 2
print(a)

# Integer
b = 9223372036854775807
print(b)

# Floating point
pi = 3.14
print(pi)

# String
c = 'A'
print(c)

# String
name = 'John Doe'
print(name)

# Boolean
q = True
print(q)

# Empty value or null data type
x = None
print(x)
print("there's no need to specify a data type when declaring a variable in Python.Here we find datatype of varibles")
a = 2
print(type(a))
# Output: <type 'int'>
b = 9223372036854775807
print(type(b))
# Output: <type 'int'>
pi = 3.14
print(type(pi))
# Output: <type 'float'>
c = 'A'
print(type(c))
# Output: <type 'str'>
name = 'John Doe'
print(type(name))
# Output: <type 'str'>
q = True
print(type(q))
print("assign multiple values to multiple variables in one line")
a, b, c = 1, 2, 3
print(a, b, c)

x = y = [7, 8, 9] # x and y are two different names for the same list object just created, [7,8, 9]
x[0] = 13 # we are updating the value of the list [7, 8, 9] through one of its names, x in this case
print(y)



