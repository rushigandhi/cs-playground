# Implemenation of a Queue data structure as a Linked List


class Node:
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.next = None


class Stack():

    def __init__(self):
        self.top = None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            return temp
        return None

    def peek(self):
        if not self.isEmpty():
            return self.top
        return None

    def isEmpty(self):
        return self.top == None

    def print(self):
        curr_node = self.top
        output = ''
        while curr_node:
            output += str(curr_node.value) + " -> "
            curr_node = curr_node.next
        return output

    def nuke(self):
        # Due to Python's implicit memory management, we cannot manually delete all the nodes
        # Setting front and rear to None should suffice
        self.top = None
