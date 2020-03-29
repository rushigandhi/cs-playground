from LinkedList import LinkedList
from LinkedList import Node


def test_linked_list():

    # make initial nodes
    node_1 = Node(2)
    node_2 = Node(24)
    node_3 = Node(-31)
    node_4 = Node(0)

    # test append()
    ll = LinkedList(node_1)
    ll.append(node_2)
    ll.append(node_3)
    ll.append(node_4)
    assert ll.print() == '2 -> 24 -> -31 -> 0 -> '

    # test get_position_of_value()
    assert ll.get_position_of_value(2) == 0
    assert ll.get_position_of_value(24) == 1
    assert ll.get_position_of_value(-31) == 2
    assert ll.get_position_of_value(0) == 3
    assert ll.get_position_of_value(-32) == -1

    # test insert()
    node_5 = Node(99)
    node_6 = Node(-4.5)
    node_7 = Node(100000)
    ll.insert(node_5, 1)
    ll.insert(node_6, 3)
    ll.insert(node_7, 4)
    assert ll.print() == '2 -> 99 -> 24 -> -4.5 -> 100000 -> -31 -> 0 -> '

    # test get_node_at_position()
    assert ll.get_node_at_position(3) == node_6
    assert ll.get_node_at_position(1) == node_5
    assert ll.get_node_at_position(5) == node_3

    # test delete()
    ll.delete(99)
    assert ll.print() == '2 -> 24 -> -4.5 -> 100000 -> -31 -> 0 -> '
    ll.delete(0)
    ll.delete(2)
    ll.delete(24)
    assert ll.print() == '-4.5 -> 100000 -> -31 -> '
    node_8 = Node(-31)
    ll.insert(node_8, 1)
    assert ll.print() == '-4.5 -> -31 -> 100000 -> -31 -> '
    assert ll.get_position_of_value(-31) == 1
    assert ll.get_node_at_position(1) == node_8
    assert ll.get_node_at_position(5) == None
    assert ll.get_node_at_position(3) == node_3
    ll.delete(-31)
    assert ll.print() == '-4.5 -> 100000 -> -31 -> '
    ll.delete(-31)
    assert ll.print() == '-4.5 -> 100000 -> '
    ll.delete(-4.5)
    assert ll.print() == '100000 -> '
    ll.delete(100000)
    assert ll.print() == ''

    # test nuke()
    node_9 = Node(9)
    ll.append(node_9)
    assert ll.print() == '9 -> '
    ll.nuke()
    assert ll.print() == ''
