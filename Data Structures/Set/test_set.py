from Set import Set


def test_set():

    # initialize set
    set_A = Set()

    # test add()
    set_A.add(2)
    set_A.add(2)
    set_A.add(3)
    set_A.add(-526)
    assert set_A.to_string() == '[2, 3, -526]'

    # test has()
    assert set_A.has(3) == True
    assert set_A.has(4) == False
    assert set_A.has(2) == True
    assert set_A.has(-526) == True

    # test cardinality()
    assert set_A.cardinality() == 3

    # test update()
    set_A.update([])
    assert set_A.to_string() == '[2, 3, -526]'
    set_A.update([2, 3, 4])
    assert set_A.to_string() == '[2, 3, -526, 4]'

    # test remove()
    set_A.remove(2)
    set_A.remove(3)
    assert set_A.to_string() == '[-526, 4]'
    set_A.remove(-526)
    set_A.remove(4)
    assert set_A.to_string() == '[]'
    set_A.remove(100)
    assert set_A.to_string() == '[]'

    # test union()
    set_B = Set()
    set_B.update([5, 2, 743, 21, 3, 9])
    set_A.update([2, 3, -526, 4])
    set_union = set_A.union(set_B)
    assert set_union.to_string() == '[2, 3, -526, 4, 5, 743, 21, 9]'

    # test intersection()
    set_intersection = set_A.intersection(set_B)
    assert set_intersection.to_string() == '[2, 3]'

    # test difference()
    set_difference = set_A.difference(set_B)
    assert set_difference.to_string() == '[-526, 4]'

    # test is_subset()
    set_C = Set()
    set_C.update([2, 3])
    assert set_C.is_subset(set_A) == True
    assert set_C.is_subset(set_B) == True
    set_difference.add(2)
    assert set_C.is_subset(set_difference) == False

    # test is_proper_subset()
    set_D = Set()
    set_D.update([3, 3, 2])
    assert set_C.is_proper_subset(set_A) == True
    assert set_C.is_proper_subset(set_B) == True
    assert set_C.is_proper_subset(set_D) == False
    assert set_C.is_proper_subset(set_C) == False

    # test is_superset()
    assert set_A.is_superset(set_C) == True
    assert set_B.is_superset(set_C) == True
    assert set_C.is_superset(set_A) == False
