from node import Node

class Queue:
	def __init__(self):
		self.first = None
		self.last = None

	def enqueue(self, value):
		node = Node(value)

		if self.last is not None:
			self.last.next = node
			self.last = node
		else:
			self.first = node
			self.last = node

	def dequeue(self):
		if self.first is not None:
			tmp = self.first
			self.first = self.first.next
			return tmp
		else:
			return None

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

# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# print(q)
# print(q.dequeue())
# print(q)