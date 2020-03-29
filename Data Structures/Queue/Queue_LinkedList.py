# node element that the queue is composed of
class Node:
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.next = None


# implemenation of a queue data structure as a linked list
class Queue():

    # initialize by setting the front and rear pointers to None
    def __init__(self):
        self.front = self.rear = None

    # enqueue a new_node to the end of the queue, (worst case O(1))
    def enqueue(self, new_node):

        # if the queue is empty make front the new_node
        if self.is_empty():
            self.front = new_node

        # otherwise, append the new_node to the end of rear
        else:
            self.rear.next = new_node

        # make rear the new_node
        self.rear = new_node

    # dequeue a node from the front of the queue (worst case O(1))
    def dequeue(self):
        if not self.is_empty():

            # remove node from the front of the queue
            temp = self.front
            self.front = self.front.next

            # if list is now empty, both front and rear should be None
            if self.front == None:
                self.rear = None
            return temp
        return None

    # peek by returning front (worst case O(1))
    def peek(self):
        if not self.is_empty():
            return self.front
        return None

    # is_empty checks if front is None
    def is_empty(self):
        return self.front == None

    # to_string by returning a string version of queue
    def to_string(self):
        curr_node = self.front
        output = ''
        while curr_node:
            output += str(curr_node.value) + " -> "
            curr_node = curr_node.next
        return output

    # nuke by removing access to front and rear
    def nuke(self):
        # Due to Python's implicit memory management, we cannot manually delete all the nodes
        # Setting front and rear to None should suffice
        self.front = None
        self.rear = None
