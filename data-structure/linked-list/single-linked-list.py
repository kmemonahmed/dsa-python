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
        print(list_str + '\n')

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

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        if prev:
            self.head = prev

    def remove_first_element(self):
        if self.head:
            self.head = self.head.next

    def remove_last_element(self):
        if self.head:
            head_copy = self.head
            prev = None
            while head_copy.next:
                prev = head_copy
                head_copy = head_copy.next
            
            if prev:
                prev.next = None
            else:
                self.head = None

    def remove_element(self, data):
        if self.head:
            if self.head.val == data:
                self.head = self.head.next
            else:
                head_copy = self.head
                while head_copy:
                    if head_copy.next and head_copy.next.val == data:
                        head_copy.next = head_copy.next.next
                        break
                    else:
                        head_copy = head_copy.next

                if head_copy == None:
                    print('Item not found in linked list!')

        else:
            print("Linked list is empty!")

    def remove_element_method_2(self, data):
        if self.head:
            if self.head.val == data:
                self.head = self.head.next
            else:
                head_copy = self.head
                while head_copy:
                    if head_copy.val == data:
                        break
                    prev = head_copy
                    head_copy = head_copy.next

                if head_copy == None:
                    print('Item not found in linked list!')
                else:
                    prev.next = head_copy.next
                    head_copy = None

        else:
            print("Linked list is empty!")



list_1 = SingleLinkedList()
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



# insert after 2
middle_node = list_1.find_node(2)
if middle_node:
    list_1.insert_in_between(middle_node, 5)
    print('Insert 5 after node.val 2')
    list_1.print_linked_list()
else:
    print('Middle node not found')

list_1.reverse()
print('Reverse Linked List')
list_1.print_linked_list()

list_1.reverse()
print('Reverse back Linked List')
list_1.print_linked_list()


list_1.remove_first_element()
print('Remove first element')
list_1.print_linked_list()

list_1.remove_last_element()
print('Remove Last Element')
list_1.print_linked_list()

list_1.remove_element(5)
print('Remove 5 from linked list')
list_1.print_linked_list()

list_1.remove_element_method_2(3)
print('Remove 3 from linked list')
list_1.print_linked_list()

list_1.remove_element(2)
print('Remove 2 from linked list')
list_1.print_linked_list()

print('-----------xxxx------------------------')