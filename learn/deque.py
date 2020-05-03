import collections

de = collections.deque([1, 2, 3])
de.append(4)
print("deque after append")
print(de)
de.appendleft(0)
print("deque after appendleft")
print(de)
de.pop()
print("deque after pop")
print(de)
de.popleft()
print("deque after pop left")
print(de)
print(de.index(2, 0, len(de)))  # index(ele, beg, end)
de2 = collections.deque([1, 2, 5, 2, 4, 6, 7, 1, 4])
print(de2.index(2, 2, 5))
de2.insert(2, 1)
print("de2 after insert 2 at index of 1")
print(de2)
print("count of 2 in de2")
print(de2.count(2))
print("de2 after removing 4 from first occurance")
de2.remove(4)
print(de2)
# using extend() to add numbers to right end  
# adds 4,5,6 to right end 
de.extend([4,5,6]) 
  
# printing modified deque 
print ("The deque after extending deque at end is : ") 
print (de) 
  
# using extendleft() to add numbers to left end  
# adds 7,8,9 to right end 
de.extendleft([7,8,9]) 
  
# printing modified deque 
print ("The deque after extending deque at beginning is : ") 
print (de) 
  
# using rotate() to rotate the deque 
# rotates by 3 to left 
de.rotate(-3) 
  
# printing modified deque 
print ("The deque after rotating deque is : ") 
print (de) 
  
# using reverse() to reverse the deque 
de.reverse() 
  
# printing modified deque 
print ("The deque after reversing deque is : ") 
print (de) 