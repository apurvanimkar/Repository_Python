from collections import deque
  
# initializing deque 
de = deque([6, 1, 2, 3, 4])
  
# deletes 4 from the right end of deque 
de.pop()
print("after pop-",de)
    
# deletes 6 from the left end of deque 
de.popleft()
print("after pop-",de)

#appending at right side   
print(de.append(44))
print("after append-",de)
    
# inserts 6 at the beginning of deque 
de.appendleft(10)
print("after append-",de)
    
