# Implemenation of a Queue data structure as a Linked List


class Node:
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.next = None


class Queue():

    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):
        if self.isEmpty():
            self.front = new_node
        else:
            self.rear.next = new_node

        self.rear = new_node

    def dequeue(self):
        if not self.isEmpty():
            temp = self.front
            self.front = self.front.next

            if self.front == None:
                self.rear = None
            return temp
        return None

    def peek(self):
        if not self.isEmpty():
            return self.front
        return None

    def isEmpty(self):
        return self.front == None

    def print(self):
        curr_node = self.front
        output = ''
        while curr_node:
            output += str(curr_node.value) + " -> "
            curr_node = curr_node.next
        return output

    def nuke(self):
        # Due to Python's implicit memory management, we cannot manually delete all the nodes
        # Setting front and rear to None should suffice
        self.front = None
        self.rear = None
