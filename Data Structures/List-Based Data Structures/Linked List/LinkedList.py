class Node:
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        curr_node = self.head
        if self.head:
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
        else:
            self.head = new_node

    def get_position_of_value(self, value):
        position = 0
        curr_node = self.head

        while curr_node:
            if curr_node.value == value:
                return position
            curr_node = curr_node.next
            position += 1
        return -1

    def get_node_at_position(self, position):
        counter = 0
        curr_node = self.head

        if position >= 0:
            while curr_node and counter <= position:
                if counter == position:
                    return curr_node
                curr_node = curr_node.next
                counter += 1
            return None
        else:
            return None

    def insert(self, new_node, position):
        counter = 0
        curr_node = self.head

        if position > 0:
            while curr_node and counter < position:
                if counter == position - 1:
                    new_node.next = curr_node.next
                    curr_node.next = new_node
                    return

                curr_node = curr_node.next
                counter += 1
        elif position == 0:
            new_node.next = self.head
            self.head = new_node

    def delete(self, value):
        curr_node = self.head

        if self.head:
            if curr_node.value == value:
                self.head = curr_node.next
                return
            while curr_node.next:
                if curr_node.next.value == value:
                    curr_node.next = curr_node.next.next
                    return
                curr_node = curr_node.next
        else:
            return

    def print(self):
        curr_node = self.head
        output = ''
        while curr_node:
            output += str(curr_node.value) + " -> "
            curr_node = curr_node.next
        return output

    def nuke(self):
        # Due to Python's implicit memory management, we cannot manually delete all the nodes
        # Setting the head to None should suffice
        self.head = None
