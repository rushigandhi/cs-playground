# this is the class for a bucket which stores the data in a hash table
class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# this is an implementation of a hash table using open hashing with chaining
# Basic Idea: if a bucket is not empty, add the new node to the end of the LinkedList in that bucket
class HashTable():

    # initialize storage and set number_of_active_elements to 0
    def __init__(self, size):
        self.storage = [None] * size

    # get_hash is calculated as the remainder of the division of the key by the number of buckets
    def get_hash(self, key, number_of_buckets):
        return key % number_of_buckets

    # store will insert/update the value for a specific key
    def store(self, key, value):

        # get the number of buckets, index of the input key, and the corresponding bucket
        number_of_buckets = len(self.storage)
        index = self.get_hash(key, number_of_buckets)
        curr_node = self.storage[index]

        # if bucket is empty, made this node the start of the linked list
        if not curr_node:
            curr_node = Node(key, value)

        # traverse the list to get the to end of the list
        else:
            while curr_node and curr_node.next:

                # if key already exists, update the value
                if curr_node.key == key:
                    curr_node.value = value
                    return

            # add the new node to the end of the list
            curr_node.next = Node(key, value)

    # has returns if the input key and it's respective data is in the hash table
    def has(self, key):

        # get the number of buckets, index of the input key, and the corresponding bucket
        number_of_buckets = len(self.storage)
        index = self.get_hash(key, number_of_buckets)
        curr_node = self.storage[index]

        # traverse until you find the key
        while curr_node:
            if curr_node.key == key:
                return True
            curr_node = curr_node.next

        return False

    # lookup returns the value for that specific input key
    def lookup(self, key):

        # get the number of buckets, index of the input key, and the corresponding bucket
        number_of_buckets = len(self.storage)
        index = self.get_hash(key, number_of_buckets)
        curr_node = self.storage[index]

        # traverse until you find the key
        while curr_node:
            if curr_node.key == key:
                return curr_node.value
            curr_node = curr_node.next

        return ''

    # nuke removes all the elements from storage by setting it to an empty list
    def nuke(self):
        self.storage = []

    # to_string returns a string version of the hash table with 'index <key, value>' per line
    def to_string(self):

        number_of_buckets = len(self.storage)
        output = ''

        for i in range(number_of_buckets):

            curr_node = self.storage[i]
            while curr_node:
                output += str(i) + ' <' + \
                    self.storage[i].key + ',' + self.storage[i].value + '>\n'
                curr_node = curr_node.next
