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
            if to_travarse.prev:
                print('Prev:', to_travarse.prev.val)
            else:
                print('Prev:', None)
            print('Current:', to_travarse.val)
            if to_travarse.next:
                print('Next:', to_travarse.next.val)
            else:
                print('Next:', None)
            print(list_str + '-----------')
            
            to_travarse = to_travarse.next
        print(list_str + '\n')

    def find_node(self, data):
        current = self.head
        while current:
            if current.next:
                if current.next.val == data:
                    return current.next
            current = current.next
        return None


    def insert_at_begining(self, data):
        data = Node(data)
        data.next = self.head
        if self.head:
            self.head.prev = data
        self.head = data

    def insert_at_end(self, data):
        data = Node(data)

        if self.head:
            current = self.head
            while current.next:
                current = current.next

            data.prev = current
            current.next = data
        else:
            self.head = data


    def insert_in_between(self, prev_data, data):
        middle_node = self.find_node(prev_data)
        if middle_node:
            data = Node(data)
            data.prev = middle_node
            data.next = middle_node.next
            middle_node.next.prev = data
            middle_node.next = data
        else:
            print('Data not present in the liked list')

    def reverse(self):
        temp = None
        current = self.head

        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp:
            self.head = temp.prev


    def remove_first_element(self):
        if self.head:
            if self.head.next.prev:
                self.head.next.prev = None
            self.head = self.head.next
    

list_1 = DoublyLinkedList()
print('Initial linked list')
list_1.print_linked_list()

list_1.insert_at_begining(2)
print('Insert 2 at begining')
list_1.print_linked_list()

list_1.insert_at_begining(1)
print('Insert 1 at begining')
list_1.print_linked_list()


list_1.insert_at_end(3)
print('Insert 3 at end')
list_1.print_linked_list()

list_1.insert_at_end(4)
print('Insert 4 at end')
list_1.print_linked_list()

list_1.insert_in_between(2, 5)
print('Insert 5 after node.val 2')
list_1.print_linked_list()

list_1.reverse()
print('Reverse Linked List')
list_1.print_linked_list()

list_1.reverse()
print('Reverse back Linked List')
list_1.print_linked_list()

list_1.remove_first_element()
print('Remove first element')
list_1.print_linked_list()