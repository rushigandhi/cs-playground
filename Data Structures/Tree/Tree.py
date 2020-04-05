# Tree Node element class with a value and children pointer list
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


# implementation of a Tree class with any number of children
class Tree:

    # initialize the root node with the starting value
    def __init__(self, value):
        self.root = Node(value)

    # add the child value as a child node under the node with the parent value
    def add_child(self, parent_value, child_value, root):

        # if root is None, return
        if self.is_empty(root):
            return

        # if we found the parent, add the child to it
        elif root.value == parent_value:
            root.children.append(Node(child_value))
            return
        # else iterate through all the children and try to find the parent node
        else:
            for child in root.children:
                self.add_child(parent_value, child_value, child)

    # has checks if a value is present in the tree
    def has(self, value, root):

        # if root is None, return
        if self.is_empty(root):
            return False

        # if we found the value, return True
        if root.value == value:
            return True

        for child in root.children:
            if self.has(value, child):
                return True
        return False

    # is_empty returns if the root node is None
    def is_empty(self, root):
        return root == None

    # nuke sets the root node to None
    def nuke(self):
        self.root = None

    # preorder_traversal traverses through the tree in (parent, left -> right children) fashion
    def preorder_traversal(self, root):
        if self.is_empty(root):
            return
        output = str(root.value) + ", "
        for child in root.children:
            output += self.preorder_traversal(child)
        return output

    # postorder_traversal traverses through the tree in (left -> right children, parent) fashion
    def postorder_traversal(self, root):
        if self.is_empty(root):
            return
        output = ''
        for child in root.children:
            output += self.postorder_traversal(child)
        return output + str(root.value) + ', '
