#Indexing Tuples
x = (1, 2, 3)
print(x[0]) # 1
print(x[2]) # 3
"""print(x[3])# IndexError"""


print(x[-1])# 3
"""print(x[-4])# IndexError"""


print(x[:-1]) # (1, 2)
print(x[-1:]) # (3,)
print(x[1:3]) # (2, 3)
print("--------------------------")
#Reversing Elements
colors = "red", "green", "blue"
rev = colors[::-1]
print(rev)

rev = tuple(reversed(colors))
colors = rev
print(colors)
x=type(rev)
print(x)
x1=type(colors)
print(x1)
