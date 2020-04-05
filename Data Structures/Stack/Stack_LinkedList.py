# node element that the stack is composed of
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Implemenation of a stack data structure as a linked list
class Stack():

    # initialize by setting the top pointer to None
    def __init__(self):
        self.top = None

    # push a new_node to the top of the stack (worst case O(1))
    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    # pop a node off the top of the stack (worst case O(1))
    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            return temp
        return None

    # peek by returning the top of the stack (worst case O(1))
    def peek(self):
        if not self.is_empty():
            return self.top
        return None

    # is_empty checks if top is None
    def is_empty(self):
        return self.top == None

    # to_string by returning a string version of stack
    def to_string(self):
        curr_node = self.top
        output = ''
        while curr_node:
            output += str(curr_node.value) + " -> "
            curr_node = curr_node.next
        return output

    # nuke by removing access to top
    def nuke(self):
        # Due to Python's implicit memory management, we cannot manually delete all the nodes
        # Setting front and rear to None should suffice
        self.top = None
