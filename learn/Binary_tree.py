from binarytree import Node
from binarytree import build
from binarytree import tree
from binarytree import bst
from binarytree import heap


# creating binarytree with Node method
root = Node(3)
root.right = Node(6)
root.left = Node(8)
print("binary tree", root)
print(list(root))
print("root inorder", root.inorder)
print("size of tree: ", root.size)
print("height of tree:", root.height)
print(root.properties)


# creating binarytree with build method
node = [3, 5, 6, 8, None, 2, 9, 0, 1]
binary_tree = build(node)
print("binary tree \n ", binary_tree)


# creating binarytree with tree method
tree1 = tree()
print("tree of any height", tree1)
tree2 = tree(height=3)
print("tree of height 3", tree2)
tree3 = tree(height=3, is_perfect=True)
print("tree of height 3 and is perfect", tree3)


# creating binaty_search_tree with bst method
bsearch1 = bst()
print("tree of any height", bsearch1)
bsearch2 = bst(height=3)
print("tree of height 3", bsearch2)
bsearch3 = bst(height=3, is_perfect=False)
print("tree of height 3 and is not perfect", bsearch3)
print("inorder of tree which gives sorted list", bsearch2.inorder)


# creating heap-tree with heap method
rth = heap()
print('Max-heap of any height : \n',
      rth)

# Create a random max-heap
# of given height
rth2 = heap(height=2)

print('Max-heap of given height : \n',
      rth2)

# Create a random perfect
# min-heap of given height
rth3 = heap(height=2, is_max=False, is_perfect=True)

print('Perfect min-heap of given height : \n', rth3)

