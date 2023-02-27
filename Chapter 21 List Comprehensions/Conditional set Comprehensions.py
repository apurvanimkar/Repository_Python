#without set Comprehensions
set1=set()
for i in range(20):
    if(i%2==0):
        new_lst.append(i)
print(set1)
print()
print("-----------------")
#With set Comprehensions with conditional in "if"
set1={i for i in range(20) if i%2==0}
print("new set ="set1)
