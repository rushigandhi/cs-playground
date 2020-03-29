# Implemenation of a Queue data structure as a Python List
class Queue():

    # initialize the empty storage list
    def __init__(self):
        self.storage = []

    # enqueue by appending value to the end
    def enqueue(self, value):
        self.storage.append(value)

    # dequeue by popping value from the front
    def dequeue(self):
        if not self.is_empty():
            return self.storage.pop(0)
        return None

    # peek by returning the first value
    def peek(self):
        if not self.is_empty():
            return self.storage[0]
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
