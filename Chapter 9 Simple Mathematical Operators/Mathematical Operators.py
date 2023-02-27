print("-----------------Division------------------------")
a, b, c, d, e = 3, 2, 2.0, -3, 10
x=a / b 
print("Division=",x)
x1=a / c 
print("Division=",x1)
x2=d / b 
print("Division=",x2)
x3=b / a 
print("Division=",x3)
x4=d / e 
print("Division=",x4)

print("-----------------Addition------------------------")
a, b = 1, 2 # Using the "+" operator:
c=a + b
print(c)
print("--------------")
# Using the "in-place" "+=" operator to add and assign:
a += b # a = 3 (equivalent to a = a + b)
print(a)
print("--------------")

import operator 
operator.add(a, b) # = 5 since a is set to 3 right before this line
a = operator.iadd(a, b)
print(a)

print("-----------------Exponentiation------------------------")
a, b = 2, 3
(a ** b) # = 8
pow(a, b) # = 8
import math
a1=math.pow(a, b) # = 8.0 (always float; does not allow complex results)
print(a1)
import operator
b=operator.pow(a, b) # = 8
print(b)

import math
x = 8
c=math.pow(x, 1/3) # evaluates to 2.0
print(c)
c=x**(1/3) # evaluates to 2.0
print(c)
print("--------------")
a=math.expm1(0)
print(a)# 0.0
math.exp(1e-6) - 1 # 1.0000004999621837e-06
math.expm1(1e-6) # 1.0000005000001665e-06

print("------------------------------Trigonometric Functions---------------")
a, b = 1, 2
import math
x=math.sin(a) # returns the sine of 'a' in radians
print(x)
x=math.cosh(b) # returns the inverse hyperbolic cosine of 'b' in radians
print(x)
print("------------------------------Multiplication---------------")
a, b = 2, 3
x=a * b # = 6
print(x)
import operator
x=operator.mul(a, b) # = 6
print(x)
print("------------------------------Modulus---------------")
x=3 % 4 # 3
print(x)

import operator
x=operator.mod(3 , 4)
print(x)


