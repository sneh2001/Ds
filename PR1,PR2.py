class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def _len_(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_head(self,e):
        temp = self.head
        self.head = Node(e)
        self.head.next = temp
        self.size +=1

    def remove_head(self):
        if self.is_empty():
            print("Empty ")
            else:
                print("Occupied")
                self.head = self.head.next
                self.size +=1

    def searach (self,search_values):
        index= 0
        while(index < self.size):
            value = self.get_node_at(index)
             

























            
