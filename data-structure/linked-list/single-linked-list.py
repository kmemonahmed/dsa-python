class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        if self.head:
            data.next = self.head
            self.head = data
        else:
            self.head = data


list_1 = SingleLinkedList()
data = Node(1)
list_1.insert_at_begining(data)