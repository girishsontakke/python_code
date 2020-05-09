class Node:
   def __init__(self, val):
      self.val = val
      self.right = None
      self.left = None


class BinarySearch:
   def __init__(self):
      self.root = None
      
   def insert(self, root, node):
      if self.root is None:
         self.root = Node(node)
      else:
         if self.root.val > node:
            if self.root.right is None:
               self.root.right = node
            else:
               self.insert(root.right, node)
         else:
            if self.root.left is None:
               self.root.left = node
            else:
               self.insert(root.left, node)
   
   def inorder(self, root):
      if self.root:
         self.inorder(root.left)
         print(self.root)
         self.inorder(root.right)
   
   def search(self, root, key):
      if (self.root == key) or self.root is None:
         return self.root
      else:
         if self.root.val > key:
            self.search(self.root.left, key)
         else:
            self.search(self.root.right, key)

r = Node(50)
binarysearch = BinarySearch()
binarysearch.insert(r, 30)
binarysearch.insert(r, 20) 
binarysearch.insert(r, 40)
binarysearch.insert(r, 70)
binarysearch.insert(r, 60)
binarysearch.insert(r, 80)


print('order')
binarysearch.inorder(r)
         
   
      
             
         