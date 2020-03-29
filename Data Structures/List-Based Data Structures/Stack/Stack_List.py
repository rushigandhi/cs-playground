# Implemenation of a Stack data structure as a Python List
class Stack():

    def __init__(self):
        self.storage = []

    def push(self, new_node):
        self.storage.append(new_node)

    def pop(self):
        if not self.isEmpty():
            return self.storage.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.storage[-1]
        return None

    def isEmpty(self):
        return len(self.storage) <= 0

    def print(self):
        return str(self.storage)

    def nuke(self):
        self.storage = []
