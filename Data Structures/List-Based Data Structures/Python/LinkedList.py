from Node import Node


class LinkedList:

    def __init__(self, head=None):
        super().__init__()
        self.head = head

    def append(self, new_node):
        if self.head:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
        else:
            self.head = new_node

    def get_position(self, value):
        if self.head:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
        else:
            self.head = new_node

    def get_node(self, position):
        if self.head:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
        else:
            self.head = new_node
