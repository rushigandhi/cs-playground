from Graph import Graph
from Graph import Edge
from Graph import Node


def test_graph():

    # initialize and setup graph
    graph = Graph()
    graph.insert_edge(100, 1, 2)
    graph.insert_edge(101, 1, 3)
    graph.insert_edge(102, 1, 4)
    graph.insert_edge(103, 3, 4)

    # test get_edge_list()
    assert graph.get_edge_list() == [(
        100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]

    # test get_adjacency_list()
    assert graph.get_adjacency_list() == [None, [(
        2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]

    # test get_adjacency_matrix()
    assert graph.get_adjacency_matrix() == [[0, 0, 0, 0, 0],
                                            [0, 0, 100, 101, 102],
                                            [0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 103],
                                            [0, 0, 0, 0, 0]]
