class Node:
    def __init__(self):
        self.data = data 
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self,data):
        new_node  = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def display (self):
        currrent = self.head
        while current !=  None:
            print(current.data, end=" ")
            current = current.next
    my_list = LinkedList()
    for i in range(5):
        data = int(input())
        my_list.insert_at_end(data)
    my_list.display()
    