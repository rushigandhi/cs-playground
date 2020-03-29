from binary_search_iterative import binary_search_iterative
from binary_search_recursive import binary_search_recursive


def test_binary_search_recursive():
    assert binary_search_recursive(
        [1, 2, 3, 4, 5], 0, len([1, 2, 3, 4, 5]) - 1, 2) == 1
    assert binary_search_recursive(
        [1, 2, 3, 4, 5], 0, len([1, 2, 3, 4, 5]) - 1, -4) == -1
    assert binary_search_recursive([9, 9, 9], 0, len([9, 9, 9]) - 1, 9) == 1
    assert binary_search_recursive(
        [-9, -1, 2, 2, 5, 6, 11432], 0, len([-9, -1, 2, 2, 5, 6, 11432]) - 1, 11432) == 6
    assert binary_search_recursive(
        [-9, -1, 2, 2, 5, 6, 11432], 0, len([-9, -1, 2, 2, 5, 6, 11432]) - 1, 6) == 5
    assert binary_search_recursive(
        [-9, -1, 2, 2, 5, 6, 11432], 0, len([-9, -1, 2, 2, 5, 6, 11432]) - 1, 2) == 3


def test_binary_search_iterative():
    assert binary_search_iterative(
        [1, 2, 3, 4, 5], 0, len([1, 2, 3, 4, 5]) - 1, 2) == 1
    assert binary_search_iterative(
        [1, 2, 3, 4, 5], 0, len([1, 2, 3, 4, 5]) - 1, -4) == -1
    assert binary_search_iterative([9, 9, 9], 0, len([9, 9, 9]) - 1, 9) == 1
    assert binary_search_iterative(
        [-9, -1, 2, 2, 5, 6, 11432], 0, len([-9, -1, 2, 2, 5, 6, 11432]) - 1, 11432) == 6
    assert binary_search_iterative(
        [-9, -1, 2, 2, 5, 6, 11432], 0, len([-9, -1, 2, 2, 5, 6, 11432]) - 1, 6) == 5
    assert binary_search_iterative(
        [-9, -1, 2, 2, 5, 6, 11432], 0, len([-9, -1, 2, 2, 5, 6, 11432]) - 1, 2) == 3
