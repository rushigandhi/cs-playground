from enum import Enum


# this is the enum class for bucket types
class Status(Enum):
    EMPTY = 1
    ACTIVE = 2
    ZOMBIE = 3


# this is the class for a bucket which stores the data in a hash table
class Bucket():
    def __init__(self):
        self.key = None
        self.value = None
        self.status = Status.EMPTY


# this is an implementation of a hash table using closed hashing with linear probing
# Basic Idea: if current index is taken, find the next empty index and occupy that
class HashTable():

    # initialize storage and set number_of_active_elements to 0
    def __init__(self, size):
        self.storage = []
        self.resize(size)
        self.number_of_active_elements = 0

    # resize and fill storage with empty buckets
    def resize(self, size):
        for i in range(size):
            self.storage.append(Bucket())

    # get_hash is calculated as the remainder of the division of the key by the number of buckets
    def get_hash(self, key, number_of_buckets):
        return key % number_of_buckets

    # store will insert/update the value for a specific key
    def store(self, key, value):

        # check if there is space to add a new element
        number_of_buckets = len(self.storage)
        assert self.number_of_active_elements < number_of_buckets

        index = self.get_hash(key, number_of_buckets)

        # stop if you find a index that is not active
        while Status.ACTIVE == self.storage[index].status:

            # if the key is same, we can update it
            if self.storage[index].key == key:
                break
            index = (index + 1) % number_of_buckets

        # save the key, value pair and increment the number of active elements
        self.storage[index].key = key
        self.storage[index].value = value
        self.storage[index].status = Status.ACTIVE
        self.number_of_active_elements += 1

    # lookup_key_index returns the index at which the input key and it's respective data is stored
    def lookup_key_index(self, key):

        number_of_buckets = len(self.storage)
        index = self.get_hash(key, number_of_buckets)

        for i in range(number_of_buckets):

            # if the current index is empty
            if Status.EMPTY == self.storage[index].status:
                return -1

            # found the index that holds that key's data
            elif Status.ACTIVE == self.storage[index].status and key == self.storage[index].key:
                return index

            # if it's not a match move to the next index
            index = (index + 1) % number_of_buckets

        # made it to the end of the table, hence the input key's data does not exist
        return -1

    # has returns if the input key and it's respective data is in the hash table
    def has(self, key):
        return -1 != self.lookup_key_index(key)

    # lookup returns the value for that specific input key
    def lookup(self, key):

        index = self.lookup_key_index(key)

        if index == -1:
            return ''
        else:
            return self.storage[index].value

    # remove will eliminate that key-value pair from the hash table
    def remove(self, key):

        # set bucket's status to ZOMBIE
        index = self.lookup_key_index(key)
        self.storage[index].status = Status.ZOMBIE
        self.number_of_active_elements -= 1

    # nuke removes all the elements from storage by setting it to an empty list
    def nuke(self):
        self.storage = []

    # to_string returns a string version of the hash table with 'index <key, value>' per line
    def to_string(self):

        number_of_buckets = len(self.storage)
        output = ''

        for i in range(number_of_buckets):

            if Status.ACTIVE == self.storage[i].status:
                output += str(i) + ' <' + \
                    str(self.storage[i].key) + ',' + \
                    str(self.storage[i].value) + '>\n'
        return output
