#Combinations method in Itertools Module:

import itertools as it
a = [1,2,3,4,5]
b = list(it.combinations(a, 2))
print(b)

#we can also find all the 3-combinations:
a = [1,2,3,4,5]
b = list(it.combinations(a, 3))
print(b)
