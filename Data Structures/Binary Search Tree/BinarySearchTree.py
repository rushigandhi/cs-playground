# BST Node element class with a key, left, and right child pointer
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


'''
Implementation of a Binary Search Tree (BST)

BSTs have the same properties as normal binary trees (have at most 2 children).
However, the one defining property they follow is that the keys of all nodes in the left subtree of
any arbitrary node are less than that node's key and all the nodes in the right subtree have
keys greater than that node's key
'''


class BinarySearchTree:

    # initialize the root node to None
    def __init__(self, key):
        self.root = None

    # call the private recursive has function
    def has(self, key):
        return self.__has__(self.root, key)

    # has returns if the key is present in the BST or not
    def __has__(self, root, key):

        # if node is empty return False
        if self.is_empty(root):
            return False

        # if we found the node return True
        elif root.key == key:
            return True

        # if desired key is less than the current key, traverse through the left subtree
        elif key < root.key:
            return self.__has__(root.left, key)

        # else since the desired key is greater than the current key, traverse through the right subtree
        else:
            return self.__has__(root.right, key)

    # call the private recursive lookup function
    def lookup(self, key):
        return self.__lookup__(self.root, key)

    # lookup will return the associated data belonging to the input key
    def __lookup__(self, root, key):

        # if node is empty return the empty string
        if self.is_empty(root):
            return ''

        # if we found the node return the associated data
        elif root.key == key:
            return root.data

        # if desired key is less than the current key, traverse through the left subtree
        elif key < root.key:
            return self.__lookup__(root.left, key)

        # else since the desired key is greater than the current key, traverse through the right subtree
        else:
            return self.__lookup__(root.right, key)

    # call the private recursive insert function
    def insert(self, key, data):
        self.__insert__(self.root, key, data)

    # insert will add a new node with the input key and data to the correct location of the tree
    def __insert__(self, root, key, data):

        # if node is empty insert the node
        if self.is_empty(root):
            root = Node(key, data)

        # if desired key is less than the current key, traverse through the left subtree
        elif key < root.key:
            return self.__insert__(root.left, key, data)

        # else since the desired key is greater than the current key, traverse through the right subtree
        else:
            return self.__insert__(root.right, key, data)

    # min_value_node returns the ndoe with the smallest key in that tree
    def __min_value_node__(self, node):
        curr_node = node

        # traverse to the lowest value (leftmost leaf) in this subtree
        while curr_node.left:
            curr_node = curr_node.left
        return curr_node

    # call the private recursive delete function
    def delete(self, key):
        self.__delete__(self.root, key)

    def __delete__(self, root, key):

        # base case: if root is empty, return root
        if self.is_empty(root):
            return root

        # if we found the node, this is the one to delete
        if root.key == key:

            # case with only one child: return the node that is not empty
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            # case with two children: get the inorder successor (smallest in the right subtree)
            temp = self.__min_value_node__(root.right)

            # copy the successor's content into this node
            root.key = temp.key

            # delete the inorder successor
            root.right = self.__delete__(root.right, temp.key)

         # if desired key is less than the current key, traverse through the left subtree
        elif key < root.key:
            root.left = self.__delete__(root.left, key)

        # else since the desired key is greater than the current key, traverse through the right subtree
        else:
            root.right = self.__delete__(root.right, key)

        return root

    # call the private recursive preorder_traversal function
    def preorder_traversal(self):
        return self.__preorder_traversal__(self.root)

    # preorder_traversal traverses through the BST in (parent, left, right) fashion
    def __preorder_traversal__(self, root):
        if self.is_empty(root):
            return ''
        output = str(root.key) + ', '
        output += self.__preorder_traversal__(root.left)
        output += self.__preorder_traversal__(root.right)
        return output

    # call the private recursive postorder_traversal function
    def postorder_traversal(self):
        return self.__postorder_traversal__(self.root)

    # postorder_traversal traverses through the BST in (left, right, parent) fashion
    def __postorder_traversal__(self, root):
        if self.is_empty(root):
            return ''
        output = ''
        output += self.__postorder_traversal__(root.left)
        output += self.__postorder_traversal__(root.right)
        return output + str(root.key) + ', '

    def inorder_traversal(self):
        return self.__inorder_traversal__(self.root)

    # inorder_traversal traverses through the BST in (left, parent, right) fashion
    def __inorder_traversal__(self, root):
        if self.is_empty(root):
            return ''
        output = ''
        output += self.__postorder_traversal__(root.left)
        output += str(root.key)
        return output + self.__postorder_traversal__(root.right) + ', '

    # is_empty checks if the root is empty
    def is_empty(self):
        return self.root == None

    # nuke sets the root to None
    def nuke(self):
        self.root = None
