#List Comprehensions with Nested Loops
#without List Comprehensions
new_lst=[]
for i in range(10):
    if(i%2==0):
        new_lst.append(i)
    else:
        new_lst.append("INvalid")
print(new_lst)
print()
print("-----------------")

#With List Comprehensions in Nested loops
new_lst2=[i if i%2==0 else "Invalid" for i in range(10)]
print("new list ="new_lst2)
