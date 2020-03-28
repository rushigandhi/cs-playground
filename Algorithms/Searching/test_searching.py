from linear_search import linear_search
from binary_search import binary_search_iterative, binary_search_recursive


def test_linear_search():
    assert linear_search([1, 2, 3, 4, 5], 2) == 1
    assert linear_search([1, 2, 3, 4, 5], -4) == -1
    assert linear_search([], 0) == -1
    assert linear_search([9, 9, 9], 9) == 0
    assert linear_search([-9, 2, 5, -1, 11432, 2, 6], 11432) == 4
    assert linear_search([-9, 2, 5, -1, 11432, 2, 6], 6) == 6


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
