class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None


list_1 = SingleLinkedList()
list_1.head = Node(1)