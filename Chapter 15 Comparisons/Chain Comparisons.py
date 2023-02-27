# Python code for chaining comparison operators
x = 5
print(1 < x < 10)
print(10 < x < 20 )
print(x < 10 < x*10 < 100)
print(10 > x <= 9)
print(5 == x > 4)

#second Example
a, b, c, d, e, f = 0, 5, 12, 0, 15, 15
e1 = a <= b < c > d is not e is f #T
e2 = a is d > f is not c #F
print(e1)
print(e2)
