a = 'Python is fun!'
b = 'Python is fun!'
a == b # returns True
a is b # returns False
a = [1, 2, 3, 4, 5]
b = a # b references a
a == b # True
a is b # True
b = a[:] # b now references a copy of a
a == b # True
a is b # False [!!]
