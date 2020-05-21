class Stack(object):
	
	def __init__(self):
		self.items = []
	
	def push(self,element):
		self.items.append(element)
	
	def pop(self):
		if not self.is_empty():
			return self.items.pop()
	
	def is_empty(self):
		return len(self.items) == 0
	
	def __len__(self):
		return len(self.items)
	
	def display(self):
		return self.items
	
	def peek(self):
		if not self.is_empty():
			return self.items[-1]


