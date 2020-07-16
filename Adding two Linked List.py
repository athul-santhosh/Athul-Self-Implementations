class Node:

	def __init__(self,data):
		self.data = data
		self.next = None


class LinkedList:

	def __init__(self):
		self.head = None

	def append(self,data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node

	def display(self):
		cur = self.head
		while cur:
			print(cur.data , end = " --> ")
			cur = cur.next


	def reverse(self):
		prev = None
		cur = self.head
		while cur:
			temp = cur.next
			cur.next = prev
			prev = cur
			cur = temp
		self.head = prev





	def sumTwo(self,ListToADD): 
								                               # self is the current list, ListToADD is the List to be 
															   # added with the list
 		self.reverse()
 		ListToADD.reverse()


 		l1 = self.head
 		l2 = ListToADD.head
 		l3 = LinkedList()
 		value = 0
 		while l1 or l2 or value:

 			if l1:
 				value += l1.data
 				l1 = l1.next

 			if l2:
 				value += l2.data
 				l2 = l2.next

 			l3.append(value % 10)
 			value = value // 10
 		l3.reverse()
 		l3.display()

 			
	

L1 = LinkedList()
L1.append(1)
L1.append(2)
L1.append(9)
L1.append(3)
L1.display()


print("\n")

L2 = LinkedList()
L2.append(4)
L2.append(5)
L2.append(6)
L2.display()

print("\n")



L1.sumTwo(L2)






























