class SetClass():

    def __init__(self):
        self.storage = []

    def cardinality(self):
        return len(self.storage)

    def has(self, value):
        for element in self.storage:
            if element == value:
                return True
        return False

    def add(self, value):
        if not self.has(value):
            self.storage.append(value)

    def update(self, input_list):
        for element in input_list:
            self.add(element)

    def remove(self, value):
        if self.has(value):
            self.storage.remove(value)

    def length(self):
        return len(self.storage)

    def clear(self):
        self.storage = []

    def union(self, input_set):
        new_set = SetClass()
        for element in self.storage:
            new_set.add(element)
        for element in input_set.storage:
            new_set.add(element)
        return new_set

    def intersection(self, input_set):
        new_set = SetClass()
        for element in self.storage:
            if input_set.has(element):
                new_set.add(element)
        return new_set

    def difference(self, input_set):
        new_set = SetClass()

        for element in input_set():
            if not self.has(element):
                new_set.add(element)

        return new_set

    def is_subset(self, input_set):

        for element in self.storage:
            if not input_set.has(element):
                return False

        return True

    def is_proper_subset(self, input_set):

        for element in self.storage:
            if not input_set.has(element):
                return False

        return len(self.storage) != input_set.storage

    def is_superset(self, input_set):

        for element in input_set.storage:
            if not self.has(element):
                return False

        return True
