#without Dictionary Comprehensions
dic1={}
for i in range(20):
    if(i%2==0):
        dic1[i]=i*2
print(dic1)
print()
print("-----------------")

#With Dictionary Comprehensions with conditional in "if"
dic1={i:i*2 for i in range(20) if i%2==0}
print("new dictionary ="dic1)
