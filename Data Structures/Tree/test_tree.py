from Tree import Tree


def test_tree():

    # initialize tree
    tree = Tree("Apple")
    assert tree.preorder_traversal(tree.root) == 'Apple, '

    # test add_child, pre-order and post-order traversal
    tree.add_child('Apple', 'Pear', tree.root)
    assert tree.preorder_traversal(tree.root) == 'Apple, Pear, '
    assert tree.postorder_traversal(tree.root) == 'Pear, Apple, '
    tree.add_child('Apple', 'Orange', tree.root)
    tree.add_child('Apple', 'Grape', tree.root)
    tree.add_child('Orange', 'Mango', tree.root)
    tree.add_child('Orange', 'Peach', tree.root)
    tree.add_child('Grape', 'Watermelon', tree.root)
    assert tree.preorder_traversal(
        tree.root) == 'Apple, Pear, Orange, Mango, Peach, Grape, Watermelon, '
    assert tree.postorder_traversal(
        tree.root) == 'Pear, Mango, Peach, Orange, Watermelon, Grape, Apple, '

    # test has
    assert tree.has('Apple', tree.root)
    assert tree.has('Pear', tree.root)
    assert tree.has('Orange', tree.root)
    assert tree.has('Grape', tree.root)
    assert tree.has('Mango', tree.root)
    assert tree.has('Watermelon', tree.root)
    assert not tree.has('Pineapple', tree.root)
    assert not tree.has('Plum', tree.root)
    assert not tree.has('Kiwi', tree.root)

    # test is_empty
    assert not tree.is_empty(tree.root)
    assert tree.is_empty(None)

    # test nuke
    tree.nuke()
    assert tree.is_empty(tree.root)
