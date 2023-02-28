
from queue import Queue
q = Queue()
for x in range(1,10):
    temp = ('key', x)
    q.put(temp)

while(not q.empty()):
    item = q.get()
    print(str(item))
