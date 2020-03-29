from merge_sort import merge_sort


def test_merge_sort():
    testList = [2, 3, 1]
    merge_sort(testList)
    assert testList == [1, 2, 3]

    testList = [0, 0, 0, 0]
    merge_sort(testList)
    assert testList == [0, 0, 0, 0]

    testList = [-9, 2, 5, -1, 11432, 2, 6]
    merge_sort(testList)
    assert testList == [-9, -1, 2, 2, 5, 6, 11432]

    testList = [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]
    merge_sort(testList)
    assert testList == [1, 2, 9, 16, 21, 26,
                        27, 28, 29, 34, 39, 40, 43, 45, 46, 49]
