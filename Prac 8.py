class Node:
	
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value)
        if self.right:
            self.right.PrintTree()

    def Printpreorder(self):
        if self.value:
            print(self.value)
            if self.left:
                self.left.Printpreorder()
            if self.right:
                self.right.Printpreorder()

    def Printinorder(self):
        if self.value:
            if self.left:
                self.left.Printinorder()
            print(self.value)
            if self.right:
                self.right.Printinorder()

    def Printpostorder(self):
        if self.value:
            if self.left:
                self.left.Printpostorder()
            if self.right:
                self.right.Printpostorder()
            print(self.value)

    def insert(self, data):
        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.value:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.value = data

    def search_value(self,value):
    	if self.left:
    		self.left.search_value(value)
    	if self.value == value:
    		print("Value Found")
    		return None
    	if self.right:
        	self.right.search_value(value)
    	else:
    		print("value not found")


root = Node(12)
root.insert(13)
root.insert(14)
root.insert(15)
root.insert(16)
root.insert(17)
root.PrintTree()
print("Pre order")
root.Printpreorder()
print("In Order")
root.Printinorder()
print("Post Order")
root.Printpostorder()
root.search_value(17)
