class Node:
   def __init__(self, value):
      self.value = value
      self.right = None
      self.left = None
   
   def _insert(self, data):
      if self.value == data:
         return False
      elif self.value > data:
         if self.left:
            return self.left._insert(data)
         else:
            self.left = Node(data)
            return True
      else:
         if self.right:
            return self.right._insert(data)
         else:
            self.right = Node(data)
            return True
         
   def _inorder(self):
      if self:
         if self.left:
            self.left._inorder()
         print(str(self.value))
         if self.right:
            self.right._inorder()
      
class BinarySearchTree:
   def __init__(self):
      self.root = None
      
   def insert(self, data):
      if self.root:
         return self.root._insert(data)
      else:
         self.root = Node(data)
         return True
        
   def inorder(self):
      print("Inorder")
      self.root._inorder()

bst = BinarySearchTree()
bst.insert(10)
bst.insert(50)
bst.insert(12)
bst.insert(13)
bst.insert(10)
bst.inorder()