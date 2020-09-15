def _init_(self, data): 

        self.data = data 

        self.next = None

class LinkedList: 
    def _init_(self):
            self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
            self.head = prev 

    def Enqueue(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node 

  
 

    def printList(self):
        temp = self.head
        while(temp):
            print temp.data
            temp = temp.next

  

  


llist = LinkedList() 
llist.Enqueue(20) 
llist.Enqueue(4) 
llist.Enqueue(15) 
llist.Enqueue(85) 

  

print ("Given Linked List")
llist.printList() 
llist.reverse() 

print ("\nReversed Linked List")
llist.printList()
