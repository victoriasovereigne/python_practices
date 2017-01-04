class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

	def __str__(self):
		return self.data

class LinkedList:
	def __init__(self):
		self.first = None
		self.last = None

	def insert(self, n):
		node = Node(n)
		if self.first is None:
			self.first = node
			self.last = node
		else:
			self.last.next = node
			self.last = self.last.next

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

L = LinkedList()

L.insert(1)
L.insert(2)
L.insert(1)
L.insert(3)
L.insert(1)
L.insert(2)

print(L)
