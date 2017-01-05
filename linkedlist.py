from node import Node

class LinkedList:
	def __init__(self, array=None):
		self.first = None
		self.last = None

		if array is not None and len(array) > 0:
			for c in array:
				self.insert(c)

	def insert(self, n):
		node = Node(n)
		if self.first is None:
			self.first = node
			self.last = node
		else:
			self.last.next = node
			self.last = self.last.next

	def append(self, node):
		if self.first is None:
			print(node)
			self.first = node
			current = node

			while current.next is not None:
				current = current.next
			self.last = current
		else:
			self.last.next = node

	def __str__(self):
		if self.first is not None:
			current = self.first
			s = '['
			while current is not None:
				s += str(current.data) + ' '
				current = current.next
			s += ']'
			return s

		else:
			return '[]'
