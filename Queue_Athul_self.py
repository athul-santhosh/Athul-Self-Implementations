class Queue(object):
	
	def __init__(self):
		self.items = []
	def is_empty(self):
		return len(self.items) == 0

	def __len__(self):
		return len(self.items)

	def enqueue(self,element):
		self.items.append(element)
	
	def dequeue(self):
		if not self.is_empty():
			return self.items.pop(0)
	def peek(self):
		if not self.is_empty():
			return self.items[-1]

	def display(self):
		return self.items


# Aqueue = Queue()
# Aqueue.enqueue(1)
# Aqueue.enqueue(2)
# Aqueue.enqueue(3)
# Aqueue.enqueue(4)
# Aqueue.enqueue(5)
# Aqueue.enqueue(6)
# print(Aqueue.display())
# Aqueue.dequeue()
# print(Aqueue.display())
# Aqueue.dequeue()
# Aqueue.dequeue()
# Aqueue.dequeue()
# print(Aqueue.display())


