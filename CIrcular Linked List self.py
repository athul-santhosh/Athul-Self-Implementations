# Circular Linked List

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None


class Clinked:

	def __init__(self):
		self.head = None


	def append(self,data):

		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			new_node.next = self.head              
			return

		last_node = self.head
		head = self.head

		while last_node.next != head:
			last_node = last_node.next

		new_node.next = last_node.next
		last_node.next = new_node


	def prepend(self,data):

		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			new_node.next = self.head
			return
		last_node = self.head
		head = self.head

		while last_node.next != head:
			last_node = last_node.next

		new_node.next = last_node.next
		last_node.next = new_node
		self.head = new_node                          #the extra condition



	def lenght(self):
		count = 0
		cur = self.head
		if cur is None:
			return count
		while cur.next:
			cur = cur.next
			count += 1
			if cur == self.head:
				return count


	def delete_Elem(self,pos):
		max_ = self.lenght()
		if max_ == 0:
			print("List Empty")
			return
		if pos not in range(1,max_+1):
			print("Invalid Pos")
			return

		if pos == 1:
			if self.head.next is self.head:
				self.head.next = None
				self.head = None
				return
			else:
				cur  = self.head
				while cur.next != self.head:
					cur = cur.next
				cur.next = cur.next.next
				self.head = self.head.next
				return
				
		if pos == max_:
			cur = self.head
			temp = self.head
			while cur.next.next != temp:
				cur = cur.next
			cur.next = self.head
			return

		key = 1
		cur = self.head
		prev = None
		while key != pos:
			key += 1
			prev = cur
			cur = cur.next
		prev.next = cur.next
		cur = None

	def delete_Node(self,key):

		if self.head.data == key and self.head.next is self.head:
			self.head = None
			return
		if self.head.data == key:
			cur = self.head
			temp = self.head
			while cur.next != temp:
				cur = cur.next
			cur.next = self.head.next
			self.head = self.head.next
		else:
			cur = self.head
			prev = None
			while cur.next != self.head:
				prev = cur
				cur = cur.next
				if cur.data == key:
					prev.next = cur.next
					cur = cur.next


		


	def display(self):

		cur = self.head
		if self.lenght() == 0:
			print("List Empty")
			return

		while cur:
			print(cur.data , end = " --> ")
			cur = cur.next
			if cur == self.head:
				break


cl = Clinked()

char = "ABCDE"
for i in char:
	cl.append(i)

cl. display()
print("\n")
for i in char:
	cl.delete_Node(i)
	cl.display()
	print("\n")












