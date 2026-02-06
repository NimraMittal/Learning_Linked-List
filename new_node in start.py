class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def print_linkedlist(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

ll = LinkedList()
ll.insert_at_beginning(5)
ll.insert_at_beginning(10)
ll.insert_at_beginning(15)
ll65.print_linkedlist()