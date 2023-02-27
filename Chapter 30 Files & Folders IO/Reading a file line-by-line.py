#Reading a file line-by-line

f=open('test.txt','r')
res=f.read()
res1=f.read(4)
print(res)
print(res1)


"""#readlines()-reads one line
f=open('python.txt','r')
res=f.readline()
print(res)

#readlines()-method reads all lines and returns a list object
f=open('python.txt','r')
res=f.readlines()
print(res)"""
