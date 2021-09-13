from queue import Queue
import queue

class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BinaryTree():
	def __init__(self):
		self.root = None

	def preOrder(self, node, ans):
		if node:
			ans += str(node.data) + '-->'
			ans = self.preOrder(node.left, ans)
			ans = self.preOrder(node.right, ans)
		return ans

	def postOrder(self, node, ans):
		if node:
			ans = self.postOrder(node.left, ans)
			ans = self.postOrder(node.right, ans)
			ans += str(node.data) + '-->'
		return ans

	def inOrder(self, node, ans):
		if node:
			ans = self.inOrder(node.left, ans)
			ans += str(node.data) + '-->'
			ans = self.inOrder(node.right, ans)
		return ans