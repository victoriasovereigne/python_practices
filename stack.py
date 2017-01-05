from node import Node

class Stack:
	def __init__(self):
		self.first = None

	def isEmpty(self):
		return self.first is None

	def push(self, value):
		node = Node(value)

		if self.first is None:
			self.first = node
		else:
			tmp = self.first
			self.first = node
			self.first.next = tmp

	def peek(self):
		if self.isEmpty():
			return None
		else:
			return self.first.data

	def pop(self):
		if self.isEmpty():
			return None
		else:
			tmp = self.first
			self.first = self.first.next
			return tmp

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

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# print(stack)

# print(stack.peek())
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# print(stack)