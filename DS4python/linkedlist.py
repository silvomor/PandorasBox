from PandorasQuestions.sortingAlgorithms import selctionSort


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Linkedlist:
	def __init__(self):
		self.head = None

	def llappend(self, key):
		if self.head is None:
			self.head = Node(key)
		else:
			cur = self.head
			while cur.next:
				cur = cur.next
			cur.next = Node(key)

	def llprepend(self, key):
		if self.head is None:
			self.head = Node(key)
		else:
			temp = Node(key)
			hold = self.head
			self.head = temp
			temp.next = hold


	def print_linked_list(self):
		print('Linked List :', end=' (Head) =>')
		cur = self.head
		while cur:
			print(f' ({cur.data}) ', end = "=>")
			cur = cur.next
		print(' (Tail)')

	def list_to_linked_list(self, lst):
		for i in lst:
			self.llappend(i)

	def is_empty(self):
		if self.head is None:
			return True
		else:
			return False

	def reverse_linked_list(self):
		if not self.is_empty():
			prev, cur = None, self.head
			nex = cur.next
			while nex is not None:
				cur.next = prev
				prev = cur
				cur = nex
				nex = nex.next
			cur.next = prev
			nex = cur
			self.head = nex
		return self.head


	def length(self):
		if self.is_empty():
			return 0
		else:
			cur = self.head
			count = 0
			
			while cur.next:
				count +=1 
				cur = cur.next
			return count

	def read_this_particular_node(self, index):
		if self.is_empty():
			return None
		else:
			cur = self.head
			try:
				for i in range(0, index):
					cur = cur.next
				return cur.data
			except:
				return None

	def read_all_nodes(self):
		if self.is_empty():
			return None
		else:
			cur = self.head
			counter = 0
			try:
				while cur.next:
					state = f"{counter}th node is {cur.data}"
					print(state)
					cur = cur.next
					counter += 1
				return cur.data
			except:
				return None

	def insert_this_at_this(self, index, val):
		if self.length() < index:
			# OR WE CAN APPEND ON THE LAST POSITION
			return "Not possible, list is too short"

		if index == 0:
			self.llprepend(val)

		else:
			this_node = Node(val)
			cur = self.head
			for i in range(index-2):
				cur = cur.next
				print(i)
			hold = cur.next
			cur.next = this_node
			this_node.next = hold
		print("Result :", self.print_linked_list())
		return self.head