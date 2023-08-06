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

    def find_node(self, data):
        to_find = self.head
        while to_find:
            if to_find.val == data:
                return to_find
            else:
                to_find = to_find.next
        return None
        

    def insert_at_begining(self, data):
        data = Node(data)
        if self.head:
            data.next = self.head
            self.head = data
        else:
            self.head = data

    def insert_at_end(self, data):
        data = Node(data)
        if self.head:
            head_copy = self.head
            while head_copy.next:
                head_copy = head_copy.next
            head_copy.next = data
        else:
            self.head = data

    def insert_in_between(self, middle_node, data):
        data = Node(data)
        if middle_node:
            data.next = middle_node.next
            middle_node.next = data
        else:
            print('Middle node is not present')




list_1 = SingleLinkedList()
list_1.print_linked_list()

list_1.insert_at_begining(2)
list_1.print_linked_list()

list_1.insert_at_begining(1)
list_1.print_linked_list()

list_1.insert_at_end(3)
list_1.print_linked_list()

list_1.insert_at_end(4)
list_1.print_linked_list()

# insert after 2
middle_node = list_1.find_node(2)
if middle_node:
    list_1.insert_in_between(middle_node, 5)
    list_1.print_linked_list()
else:
    print('Middle node not found')