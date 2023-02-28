#Import module in Python

#import module_name
import math
pie = math.pi
print("The value of pi is : ",pie)

#import module_name.member_name
from math import pi    #Here we have used pi directly.
print(pi)

#from module_name import * 
from math import *
print(pi)
print(factorial(6))

#Multiple modules
import time, sockets, random

# Multiple functions
from math import sin, cos, tan

# Multiple constants
from math import pi, e

print(pi)

print(cos(45))

print(time.time())
