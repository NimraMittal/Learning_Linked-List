class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
 
    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def add_two_ll(self, head1, head2):
        curr1 = head1
        curr2 = head2
        while curr1 is not None and curr2 is not None:
            print(curr1.data+curr2.data,end = " ")
            curr1 = curr1.next
            curr2 = curr2.next

list1 = LinkedList()
list2 = LinkedList()

for i in range(5):
    data1 = int(input())
    list1.insert_at_end(data1)

for i in range(5):
    data2 = int(input())
    list2.insert_at_end(data2)

list1.add_two_ll(list1.head, list2.head)