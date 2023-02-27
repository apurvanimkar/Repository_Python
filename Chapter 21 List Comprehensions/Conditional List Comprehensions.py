#without Conditional List Comprehensions
new_lst=[]
for i in range(20):
    if(i%2==0):
        new_lst.append(i)
print(new_lst)
print()
print("-----------------")
#With Conditional List Comprehensions
new_lst2=[i for i in range(20) if i%2==0]
print("new list ="new_lst2)
