# Implemenation of a Queue data structure as a Python List
class Queue():

    def __init__(self):
        self.storage = []

    def enqueue(self, new_node):
        self.storage.append(new_node)

    def dequeue(self):
        if not self.isEmpty():
            return self.storage.pop(0)
        return None

    def peek(self):
        if not self.isEmpty():
            return self.storage[0]
        return None

    def isEmpty(self):
        return len(self.storage) <= 0

    def print(self):
        return str(self.storage)

    def nuke(self):
        self.storage = []
