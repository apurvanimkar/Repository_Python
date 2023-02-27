a = [1, 2, 3, 4, 5]
a.append(6)
a.append(7)
a.append(7)

b = [8, 9]
a.append(b)
my_string = "hello world"
a.append(my_string)
print("after appending",a)
# a: [1, 2, 3, 4, 5, 6, 7, 7, [8, 9], "hello world"]

a.extend(b)
print(a)
a.extend(range(3))
print("After extend",a)
a.insert(2, 5) # insert 5 at position 2
print("after insert",a)
a.pop(2)
print("after pop",a)
a.remove(0)
print("after remove",a)
a.reverse()
print("reversing",a)
a.count(7)
print("after count",a)
a.sort()
print("sorting",a)
