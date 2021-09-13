class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class CicularLinkedList:
	def __init__(self):
		self.head = None

	def prepend(self, data):
		newnode = Node(data)
		if not self.head:
			self.head = newnode
		else:
			cur = self.head
			newnode.next = self.head
			while cur.next != self.head:
				cur = cur.cur.next
			cur.next = newnode
			self.head = newnode

	def append(self, data):
		if not self.head:
			self.head = Node(data)
			self.head.next = self.head
		else:
			newnode = Node(data)
			cur = self.head
			while cur.next != self.head:
				cur = cur.next
			cur.next = newnode
			newnode.next = self.head

	def print_list(self):
		if not self.head:
			print("Circular Linked List is empty!")
		else:
			cur = self.head
			while cur:
				print(cur.data, end="-->")
				cur = cur.next
				if cur == self.head:
					break


