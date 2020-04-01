class Set():

    # initialize the storage list
    def __init__(self):
        self.storage = []

    # cardinality gets the number of elements in the set
    def cardinality(self):
        return len(self.storage)

    # has checks if the input value is in the set
    def has(self, value):
        for element in self.storage:
            if element == value:
                return True
        return False

    # add inserts a value into the set that isn't already in it
    def add(self, value):
        if not self.has(value):
            self.storage.append(value)

    # update inserts multiple values into the set that aren't already in it
    def update(self, input_list):
        for element in input_list:
            self.add(element)

    # remove gets rid of that value from the set
    def remove(self, value):
        if self.has(value):
            self.storage.remove(value)

    # clear removes all the elements from the set by making it an empty list
    def clear(self):
        self.storage = []

    # union returns a new set with all the elements in the current set and input_set
    def union(self, input_set):
        new_set = Set()
        for element in self.storage:
            new_set.add(element)
        for element in input_set.storage:
            new_set.add(element)
        return new_set

    # intersection returns a new set with all the elements that are in both current set and input_set
    def intersection(self, input_set):
        new_set = Set()
        for element in self.storage:
            if input_set.has(element):
                new_set.add(element)
        return new_set

    # difference returns a new set with all the elements in the current set that are not in the input_set
    def difference(self, input_set):
        new_set = Set()

        for element in self.storage:
            if not input_set.has(element):
                new_set.add(element)

        return new_set

    # is_subet returns if all the elements in the current set are in the input_set
    def is_subset(self, input_set):

        for element in self.storage:
            if not input_set.has(element):
                return False

        return True

    # is_proper_subet returns if all the elements in the current set are in the input_set
    # and both the sets are not equal
    def is_proper_subset(self, input_set):

        for element in self.storage:
            if not input_set.has(element):
                return False

        return len(self.storage) != len(input_set.storage)

    # is_superset returns if all elements in the input_set are in the current set
    def is_superset(self, input_set):

        for element in input_set.storage:
            if not self.has(element):
                return False

        return True

    # to_string returns a string version of the set
    def to_string(self):
        return str(self.storage)
