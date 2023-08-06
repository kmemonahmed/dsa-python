class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        list_str = ""
        to_travarse = self.head
        while to_travarse:
            list_str+=f"{to_travarse.val}->"
            to_travarse = to_travarse.next

        list_str+= str(None)
        print(list_str)
        

    def insert_at_begining(self, data):
        if self.head:
            data.next = self.head
            self.head = data
        else:
            self.head = data


list_1 = SingleLinkedList()
list_1.print_linked_list()
data = Node(1)
list_1.insert_at_begining(data)
list_1.print_linked_list()

data=Node(2)
list_1.insert_at_begining(data)
list_1.print_linked_list()