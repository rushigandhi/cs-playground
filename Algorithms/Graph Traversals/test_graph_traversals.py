from depth_first_search import dfs
from breadth_first_search import bfs


def test_dfs():

    # setting up the graph
    adj_mtx = [[0, 1, 1, 0],
               [0, 0, 1, 0],
               [1, 0, 0, 1],
               [0, 0, 0, 1]]

    # test dfs from different starting nodes
    assert dfs(adj_mtx, 0) == '0 2 3 1 '
    assert dfs(adj_mtx, 1) == '1 2 3 0 '
    assert dfs(adj_mtx, 2) == '2 3 0 1 '
    assert dfs(adj_mtx, 3) == '3 '


def test_bfs():

    # setting up the graph
    adj_mtx = [[0, 1, 1, 0],
               [0, 0, 1, 0],
               [1, 0, 0, 1],
               [0, 0, 0, 1]]

    # test bfs from different starting nodes
    assert bfs(adj_mtx, 0) == '0 1 2 3 '
    assert bfs(adj_mtx, 1) == '1 2 0 3 '
    assert bfs(adj_mtx, 2) == '2 0 3 1 '
    assert bfs(adj_mtx, 3) == '3 '
