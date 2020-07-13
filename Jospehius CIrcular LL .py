# Circular Linked List

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None


class Clinked:

	def __init__(self):
		self.head = None
	def __len__(self):
		return self.lenght()


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



	def delete_Node(self,node):

		if self.head == node and self.head.next is self.head:
			self.head = None
			return
		if self.head == node:
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
				if cur == node:
					prev.next = cur.next
					cur = cur.next

	def Josephius_prob(self,step):

		cur = self.head

		while len(self) > 1:

			count = 1

			while count != step:
				count += 1
				cur = cur.next
			print("The node to be removed :",cur.data)
			self.delete_Node(cur)
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
		


Jcl = Clinked()

for i in range(1,789):
	Jcl.append(i)

Jcl.Josephius_prob(2)

Jcl.display()







