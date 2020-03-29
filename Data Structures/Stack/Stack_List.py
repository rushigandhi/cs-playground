# Implemenation of a Stack data structure as a Python List
class Stack():

    # initialize the empty storage list
    def __init__(self):
        self.storage = []

    # push by appending value to the end
    def push(self, value):
        self.storage.append(value)

    # pop by popping value from the end
    def pop(self):
        if not self.is_empty():
            return self.storage.pop()
        return None

    # peek by returning the value at the end (top of stack)
    def peek(self):
        if not self.is_empty():
            return self.storage[-1]
        return None

    # is_empty checks if storage has a length less than or equal to 0
    def is_empty(self):
        return len(self.storage) <= 0

    # to_string by returning a string version of storage
    def to_string(self):
        return str(self.storage)

    # nuke by resetting to an empty list
    def nuke(self):
        self.storage = []
