#Advanced complex arithmetic

import cmath
z = 2+3j
#Exponential and logarithmic functions-
print(cmath.exp(z)) 
print(cmath.log(z))
print(cmath.log10(-100))

#Square roots:-
print(cmath.sqrt(z))

#Trigonometric functions
print(cmath.sin(z)) # (9.15449914691143-4.168906959966565j)
print(cmath.cos(z)) # (-4.189625690968807-9.109227893755337j)
print(cmath.tan(z)) # (-0.003764025641504249+1.00323862735361j)
print(cmath.asin(z)) # (0.5706527843210994+1.9833870299165355j)
print(cmath.acos(z)) # (1.0001435424737972-1.9833870299165355j)
print(cmath.atan(z)) # (1.4099210495965755+0.22907268296853878j)
print(cmath.sin(z)**2 + cmath.cos(z)**2 )# (1+0j)

#Hyperbolic functions-
print(cmath.sinh(z)) 
print(cmath.cosh(z))

