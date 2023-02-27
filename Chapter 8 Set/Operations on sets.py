print("----------------------Operations on sets--------------------")
# Union
first_set = {1, 2, 3}
second_set = {3, 4, 5}
s=first_set.union(second_set)
print(s)
first_set | second_set     # using the `|` operator

# Intersection
{1, 2, 3, 4, 5}.intersection({3, 4, 5, 6}) # {3, 4, 5}
s2={1, 2, 3, 4, 5} & {3, 4, 5, 6}
print(s2)

# Difference
{1, 2, 3, 4}.difference({2, 3, 5}) # {1, 4}
s3={1, 2, 3, 4} - {2, 3, 5} # {1, 4}
print(s3)

# Symmetric difference with
{1, 2, 3, 4}.symmetric_difference({2, 3, 5}) # {1, 4, 5}
s4={1, 2, 3, 4} ^ {2, 3, 5}
print(s4)

# Superset check
{1, 2}.issuperset({1, 2, 3}) # False
s5={1, 2} >= {1, 2, 3}
print(s5)

# Subset check
{1, 2}.issubset({1, 2, 3}) # True
s6={1, 2} <= {1, 2, 3} # True
print(s6)
print("-----------------")

# Existence check
s=2 in {1,2,3}
print(s)# True
s=4 in {1,2,3} # False
print(s)
s=4 not in {1,2,3} # True
print(s)

# Add and Remove
s = {1,2,3}
s.add(4)
print(s)# s == {1,2,3,4}
s.discard(3)
print(s)# s == {1,2,4}
s.discard(5)
print(s)# s == {1,2,4}
s.remove(2)
print(s)# s == {1,4}
s.remove(2)
print(s)# KeyError!
