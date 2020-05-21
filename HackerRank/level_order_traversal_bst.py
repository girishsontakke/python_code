import sys

class Node:
   def __init__(self,data):
      self.right=self.left=None
      self.data = data
class Solution:
   def insert(self,root,data):
      if root==None:
         return Node(data)
      else:
         if data<=root.data:
            cur=self.insert(root.left,data)
            root.left=cur
         else:
            cur=self.insert(root.right,data)
            root.right=cur
      return root
   
   def levelOrder(self, root):
      qu = []
      element_traversed = ''
      qu.append(root)
      while len(qu) > 0:
         element = qu.pop(0)
         if element.left:
            qu.append(element.left)
         if element.right:
            qu.append(element.right)
         element_traversed += str(element.data) + " "
      print(element_traversed)     
      
        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
   data=int(input())
   root=myTree.insert(root,data)
myTree.levelOrder(root)
