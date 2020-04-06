from BinarySearchTree import BinarySearchTree as BST


def test_bst():

    # initialize BST
    bst = BST(23, 'Apple')

    # test insert
    bst.insert(14, 'Pear')
    bst.insert(105, 'Orange')
    assert bst.preorder_traversal() == 'Apple, Pear, Orange, '
    assert bst.postorder_traversal() == 'Pear, Orange, Apple, '
    assert bst.inorder_traversal() == 'Pear, Apple, Orange, '
    bst.insert(65, 'Mango')
    bst.insert(2, 'Grape')
    bst.insert(34, 'Watermelon')
    bst.insert(20, 'Strawberry')

    assert bst.preorder_traversal(
    ) == 'Apple, Pear, Grape, Strawberry, Orange, Mango, Watermelon, '
    assert bst.postorder_traversal(
    ) == 'Grape, Strawberry, Pear, Watermelon, Mango, Orange, Apple, '
    assert bst.inorder_traversal(
    ) == 'Grape, Pear, Strawberry, Apple, Watermelon, Mango, Orange, '

    # test has
    assert bst.has(23)
    assert bst.has(14)
    assert bst.has(105)
    assert bst.has(2)
    assert bst.has(65)
    assert bst.has(34)
    assert not bst.has(3)
    assert not bst.has(74)
    assert not bst.has(128)

    # test lookup
    assert bst.lookup(23) == 'Apple'
    assert bst.lookup(14) == 'Pear'
    assert bst.lookup(105) == 'Orange'
    assert bst.lookup(2) == 'Grape'
    assert bst.lookup(65) == 'Mango'
    assert bst.lookup(34) == 'Watermelon'
    assert bst.lookup(106) == ''

    # test height
    assert bst.height() == 3

    # test delete
    bst.delete(23)
    assert bst.preorder_traversal(
    ) == 'Watermelon, Pear, Grape, Strawberry, Orange, Mango, '
    assert bst.postorder_traversal(
    ) == 'Grape, Strawberry, Pear, Mango, Orange, Watermelon, '
    assert bst.inorder_traversal(
    ) == 'Grape, Pear, Strawberry, Watermelon, Mango, Orange, '
    assert bst.height() == 2
    bst.delete(14)
    assert bst.preorder_traversal(
    ) == 'Watermelon, Strawberry, Grape, Orange, Mango, '
    assert bst.postorder_traversal(
    ) == 'Grape, Strawberry, Mango, Orange, Watermelon, '
    assert bst.inorder_traversal(
    ) == 'Grape, Strawberry, Watermelon, Mango, Orange, '
    assert bst.height() == 2
    bst.delete(65)
    assert bst.preorder_traversal(
    ) == 'Watermelon, Strawberry, Grape, Orange, '
    assert bst.postorder_traversal(
    ) == 'Grape, Strawberry, Orange, Watermelon, '
    assert bst.inorder_traversal(
    ) == 'Grape, Strawberry, Watermelon, Orange, '
    bst.delete(20)
    assert bst.preorder_traversal(
    ) == 'Watermelon, Grape, Orange, '
    assert bst.postorder_traversal(
    ) == 'Grape, Orange, Watermelon, '
    assert bst.inorder_traversal(
    ) == 'Grape, Watermelon, Orange, '
    bst.insert(120, 'Blueberry')
    bst.delete(34)
    assert bst.preorder_traversal(
    ) == 'Orange, Grape, Blueberry, '
    assert bst.postorder_traversal(
    ) == 'Grape, Blueberry, Orange, '
    assert bst.inorder_traversal(
    ) == 'Grape, Orange, Blueberry, '
    assert bst.height() == 1
    bst.delete(120)
    bst.delete(2)
    bst.delete(105)
    assert bst.preorder_traversal(
    ) == ''
    assert bst.postorder_traversal(
    ) == ''
    assert bst.inorder_traversal(
    ) == ''
    assert bst.height() == 0

    # test is_empty
    assert bst.is_empty(bst.root)
    assert bst.is_empty(None)
    bst = BST(43, 'Blackberry')
    assert not bst.is_empty(bst.root)

    # test nuke
    bst.nuke()
    assert bst.is_empty(bst.root)
