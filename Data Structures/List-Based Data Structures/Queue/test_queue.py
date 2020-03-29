from Queue_List import Queue as QueueL
from Queue_LinkedList import Queue as QueueLL
from Queue_LinkedList import Node


def test_queue_list():

    # initialize stack
    queue = QueueL()

    # test enqueue()
    queue.enqueue(2)
    queue.enqueue(24)
    queue.enqueue(-31)
    queue.enqueue(0)
    assert queue.print() == '[2, 24, -31, 0]'

    # test dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.print() == '[-31, 0]'
    queue.dequeue()
    queue.dequeue()
    assert queue.print() == '[]'
    queue.dequeue()

    # test peek()
    queue.enqueue(7)
    queue.enqueue(-1)
    assert queue.peek() == 7
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.peek() == None
    assert queue.print() == '[]'

    # test isEmpty()
    assert queue.isEmpty()
    queue.enqueue(10)
    assert not queue.isEmpty()

    # test nuke()
    assert queue.print() == '[10]'
    queue.nuke()
    assert queue.isEmpty()
    assert queue.print() == '[]'


def test_queue_linked_list():

    # initialize nodes and queue
    node_1 = Node(2)
    node_2 = Node(24)
    node_3 = Node(-31)
    node_4 = Node(0)
    queue = QueueLL()

    # test enqueue()
    queue.enqueue(node_1)
    queue.enqueue(node_2)
    queue.enqueue(node_3)
    queue.enqueue(node_4)
    assert queue.print() == '2 -> 24 -> -31 -> 0 -> '

    # test dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.print() == '-31 -> 0 -> '
    queue.dequeue()
    queue.dequeue()
    assert queue.print() == ''
    queue.dequeue()

    # test peek()
    node_5 = Node(7)
    node_6 = Node(-1)
    queue.enqueue(node_5)
    queue.enqueue(node_6)
    assert queue.peek() == node_5
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.peek() == None
    assert queue.print() == ''

    # test isEmpty()
    assert queue.isEmpty()
    node_7 = Node(10)
    queue.enqueue(node_7)
    assert not queue.isEmpty()

    # test nuke()
    assert queue.print() == '10 -> '
    queue.nuke()
    assert queue.isEmpty()
    assert queue.print() == ''
