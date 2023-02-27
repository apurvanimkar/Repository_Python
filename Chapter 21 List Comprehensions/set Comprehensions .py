
#without Set Comprehensions
new_set=set()
for i in range(10):
    new_lst.append(i+1)
print(new_set)

print("-----------------")

#With set Comprehensions 
new_lst2={i+1 for i in range(10)}
print("new list ="new_lst2)
