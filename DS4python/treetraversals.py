from binarytree import *

tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print('PreOrder: ', tree.preOrder(tree.root, ''))
print('PostOrder: ', tree.postOrder(tree.root, ''))
print('InOrder: ', tree.inOrder(tree.root, ''))
