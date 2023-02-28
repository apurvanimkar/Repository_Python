
from collections import Counter

c = Counter(["a", "b", "c", "d", "a", "b", "a", "c", "d"])

# O/p:({'a': 3, 'b': 2, 'c': 2, 'd': 2})

print(c["a"])#3

print(c[7])# 0
print("----------------------------------------------------")
#Counting the occurrences of one item in a sequence: list.count() and tuple.count()
#list:--
alist = [1, 2, 3, 4, 1, 2, 1, 3, 4]
print(alist.count(1))
# O/p- 3

#Tuple:--
atuple = ('bear', 'weasel', 'bear', 'frog')
print(atuple.count('bear'))
# O/p-2
print(atuple.count('fox'))
# O/p- 0
