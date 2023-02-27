#without List Comprehension
new_lst=[]
for i in range(20):
    new_lst.append(i+1)

print(new_lst)
print("-----------------")
#With List Comprehension
new_lst2=[i+1 for i in range(20)]
print(new_lst2)
