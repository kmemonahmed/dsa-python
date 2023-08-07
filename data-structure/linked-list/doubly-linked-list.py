class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        list_str = ""
        to_travarse = self.head
        while to_travarse:
            list_str+=f"{to_travarse.val}->"
            to_travarse = to_travarse.next

        list_str+= str(None)
        print(list_str + '\n')

    def insert_at_begining(self, data):
        data = Node(data)
        data.next = self.head
        if self.head:
            self.head.prev = data
        self.head = data


list_1 = DoublyLinkedList()
print('Initial linked list')
list_1.print_linked_list()

list_1.insert_at_begining(2)
print('Insert 2 at begining')
list_1.print_linked_list()

list_1.insert_at_begining(1)
print('Insert 1 at begining')
list_1.print_linked_list()
