from Stack_List import Stack as StackL
from Stack_LinkedList import Stack as StackLL
from Stack_LinkedList import Node


def test_stack_list():

    # initialize stack
    stack = StackL()

    # test push()
    stack.push(2)
    stack.push(24)
    stack.push(-31)
    stack.push(0)
    assert stack.print() == '[2, 24, -31, 0]'

    # test pop()
    stack.pop()
    stack.pop()
    assert stack.print() == '[2, 24]'
    stack.pop()
    stack.pop()
    assert stack.print() == '[]'
    stack.pop()

    # test peek()
    stack.push(7)
    stack.push(-1)
    assert stack.peek() == -1
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.peek() == None
    assert stack.print() == '[]'

    # test isEmpty()
    assert stack.isEmpty()
    stack.push(10)
    assert not stack.isEmpty()

    # test nuke()
    assert stack.print() == '[10]'
    stack.nuke()
    assert stack.isEmpty()
    assert stack.print() == '[]'


def test_stack_linked_list():

    # initialize nodes and stack
    node_1 = Node(2)
    node_2 = Node(24)
    node_3 = Node(-31)
    node_4 = Node(0)
    stack = StackLL()

    # test push()
    stack.push(node_1)
    stack.push(node_2)
    stack.push(node_3)
    stack.push(node_4)
    assert stack.print() == '0 -> -31 -> 24 -> 2 -> '

    # test pop()
    stack.pop()
    stack.pop()
    assert stack.print() == '24 -> 2 -> '
    stack.pop()
    stack.pop()
    assert stack.print() == ''
    stack.pop()

    # test peek()
    node_5 = Node(7)
    node_6 = Node(-1)
    stack.push(node_5)
    stack.push(node_6)
    assert stack.peek() == node_6
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.peek() == None
    assert stack.print() == ''

    # test isEmpty()
    assert stack.isEmpty()
    node_7 = Node(10)
    stack.push(node_7)
    assert not stack.isEmpty()

    # test nuke()
    assert stack.print() == '10 -> '
    stack.nuke()
    assert stack.isEmpty()
    assert stack.print() == ''
