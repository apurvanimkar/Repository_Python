# Python program to show bitwise operators
 
a = 10
b = 4
 
# Print bitwise AND operation
print("a & b =", a & b)
 
# bitwise OR operation
print("a | b =", a | b)
 
# bitwise NOT operation
print("~a =", ~a)
 
# bitwise XOR operation
print("a ^ b =", a ^ b)

#second Example:


a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print("Value of c is ", c)

c = a | b;        # 61 = 0011 1101 
print("Value of c is ", c)

c = a ^ b;        # 49 = 0011 0001
print ("Value of c is ", c)

c = ~a;           # -61 = 1100 0011
print ("Value of c is ", c)

c = a << 2;       # 240 = 1111 0000
print ("Value of c is ", c)

c = a >> 2;       # 15 = 0000 1111
print ("Value of c is ", c)
