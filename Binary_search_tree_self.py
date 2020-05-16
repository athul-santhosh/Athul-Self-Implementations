class Node:
    def __init__(self,data =None):
        self.data = data
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)        #self.root --> cur_node
    
    def _insert(self,data,cur_node):
        if data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data,cur_node.right)
        elif data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data,cur_node.left)

        else:
            print("The element is already present in the Tree")

    def find(self,data):
        if self.root is None:
            return None
        else:
            is_present = self._find(data,self.root)
            if is_present:
                return True
            return False

    def _find(self,data,cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                return False
            else:
                return self._find(data,cur_node.left)
        if data > cur_node.data:
            if cur_node.right is None:
                return False
            else:
                return self._find(data,cur_node.right)
        if data == cur_node.data:
            return True

bst = BST()
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.insert(45)
bst.insert(37)
print(bst.find(37))



    


