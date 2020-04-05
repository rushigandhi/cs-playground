# LinkedList Node element class with a value and next element pointer
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    # initialize LinkedList by setting the head
    def __init__(self, head=None):
        self.head = head

    # append new_node to the end of the LinkedList (worst case O(n))
    def append(self, new_node):
        curr_node = self.head
        # if head exists, find the last node and make new_node it's next element
        if self.head:
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
        # else, make head the new_node
        else:
            self.head = new_node

    # get the position of a certain value in the LinkedList (worst case O(n))
    def get_position_of_value(self, value):
        position = 0
        curr_node = self.head

        # traverse until curr_node's value is equal to the desired value
        while curr_node:
            if curr_node.value == value:
                return position

            # increment position to keep track of where we are in the LinkedList
            position += 1
            curr_node = curr_node.next
        return -1

    # get node at desired position (worst case O(n))
    def get_node_at_position(self, position):
        position_counter = 0
        curr_node = self.head

        if position >= 0:
            # traverse until position_counter == position
            while curr_node and position_counter <= position:
                if position_counter == position:
                    return curr_node

                # increment position_counter to keep track of where we are in the LinkedList
                position_counter += 1
                curr_node = curr_node.next
            return None
        else:
            return None

    # insert new_node at specified position (worst case O(n))
    def insert(self, new_node, position):
        position_counter = 0
        curr_node = self.head

        if position > 0:

            # traverse until position_counter == position - 1, to get the previous node
            while curr_node and position_counter < position:
                if position_counter == position - 1:

                    # insert new_node between curr_node and it's next node
                    new_node.next = curr_node.next
                    curr_node.next = new_node
                    return

                # increment position_counter to keep track of where we are in the LinkedList
                curr_node = curr_node.next
                position_counter += 1

        # if position is 0, make head equal to new_node
        elif position == 0:
            new_node.next = self.head
            self.head = new_node

    # Delete a specific value (worst case O(n))
    def delete(self, value):
        curr_node = self.head

        if self.head:

            # if head.value is equal to value, delete head
            if curr_node.value == value:
                self.head = curr_node.next
                return

            # traverse until curr_node.next's value is equal to the desired value
            while curr_node.next:
                if curr_node.next.value == value:
                    curr_node.next = curr_node.next.next
                    return
                curr_node = curr_node.next
        else:
            return

    # Return a string version of the LinkedList
    def to_string(self):
        curr_node = self.head
        output = ''
        while curr_node:
            output += str(curr_node.value) + " -> "
            curr_node = curr_node.next
        return output

    # Destroy access to the LinkedList
    def nuke(self):
        # Due to Python's implicit memory management, we cannot manually delete all the nodes
        # Setting the head to None should suffice
        self.head = None
