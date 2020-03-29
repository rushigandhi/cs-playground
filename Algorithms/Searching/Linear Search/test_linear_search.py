from linear_search import linear_search


def test_linear_search():
    assert linear_search([1, 2, 3, 4, 5], 2) == 1
    assert linear_search([1, 2, 3, 4, 5], -4) == -1
    assert linear_search([], 0) == -1
    assert linear_search([9, 9, 9], 9) == 0
    assert linear_search([-9, 2, 5, -1, 11432, 2, 6], 11432) == 4
    assert linear_search([-9, 2, 5, -1, 11432, 2, 6], 6) == 6
