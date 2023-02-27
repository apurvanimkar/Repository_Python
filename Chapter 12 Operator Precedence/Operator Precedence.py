a, b, c, d = 2, 3, 5, 7
x=a ** (b + c) # parentheses
print(x)

x=a * b ** c # exponent: same as `a * (b ** c)`
print(x)

x=a + b * c / d # mul/div: same as `a + (b * c / d)`
print(x)
