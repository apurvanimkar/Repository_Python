#Using the third "step" argument
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
lst[::2]     #['a', 'c', 'e', 'g']

# Selecting a sublist from a list
lst = ['a', 'b', 'c', 'd', 'e']
lst[2:4]     #['c', 'd']
lst[2:]      #['c', 'd', 'e']
lst[:4]      #['a', 'b', 'c', 'd']

#Reversing a list with slicing
a = [1, 2, 3, 4, 5]
b = a[::-1]

# built-in list method to reverse 'a'
a.reverse()
if a = b:
    print(True)
    print(b)   #[5, 4, 3, 2, 1]
    
