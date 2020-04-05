from HashTableOpenHashing import HashTable as HashTableOH
from HashTableClosedHashing import HashTable as HashTableCH


def test_hashtable_open_hashing():

    # initialize hash table
    ht = HashTableOH(6)

    # test get_hash()
    assert ht.get_hash(21, 6) == 3
    assert ht.get_hash(3, 1) == 0
    assert ht.get_hash(42, 15) == 12

    # test store
    ht.store(2, 'hi')
    ht.store(3, 'my')
    ht.store(21, 'name')
    ht.store(5, 'is Rushi')
    assert ht.to_string() == '2 <2,hi>\n3 <3,my>\n3 <21,name>\n5 <5,is Rushi>\n'
    # update value for key 5
    ht.store(5, 'is not Rushi')
    ht.store(2, 'hello')
    assert ht.to_string() == '2 <2,hello>\n3 <3,my>\n3 <21,name>\n5 <5,is not Rushi>\n'

    # test has
    assert ht.has(2)
    assert ht.has(3)
    assert ht.has(21)
    assert ht.has(5)
    assert not ht.has(4)
    assert not ht.has(22)

    # test lookup
    assert ht.lookup(2) == 'hello'
    assert ht.lookup(3) == 'my'
    assert ht.lookup(21) == 'name'
    assert ht.lookup(5) == 'is not Rushi'
    assert ht.lookup(22) == ''

    # test remove
    ht.remove(2)
    ht.remove(3)
    assert ht.to_string() == '3 <21,name>\n5 <5,is not Rushi>\n'
    ht.store(9, "you're")
    ht.store(33, 'welcome')
    assert ht.to_string() == "3 <21,name>\n3 <9,you're>\n3 <33,welcome>\n5 <5,is not Rushi>\n"
    ht.remove(9)
    assert ht.to_string() == '3 <21,name>\n3 <33,welcome>\n5 <5,is not Rushi>\n'
    ht.remove(21)
    assert ht.to_string() == '3 <33,welcome>\n5 <5,is not Rushi>\n'
    ht.remove(33)
    assert ht.to_string() == '5 <5,is not Rushi>\n'
    ht.remove(5)
    assert ht.to_string() == ''
    ht.store(9, "you're")
    assert ht.to_string() == "3 <9,you're>\n"

    # test nuke
    ht.nuke()
    assert ht.to_string() == ''


def test_hashtable_closed_hashing():

    # initialize hash table
    ht = HashTableCH(6)

    # test get_hash()
    assert ht.get_hash(21, 6) == 3
    assert ht.get_hash(3, 1) == 0
    assert ht.get_hash(42, 15) == 12

    # test store
    ht.store(2, 'hi')
    ht.store(3, 'my')
    ht.store(21, 'name')
    ht.store(5, 'is Rushi')
    assert ht.to_string() == '2 <2,hi>\n3 <3,my>\n4 <21,name>\n5 <5,is Rushi>\n'
    # update value for key 5
    ht.store(5, 'is not Rushi')
    ht.store(2, 'hello')
    assert ht.to_string() == '2 <2,hello>\n3 <3,my>\n4 <21,name>\n5 <5,is not Rushi>\n'

    # test has
    assert ht.has(2)
    assert ht.has(3)
    assert ht.has(21)
    assert ht.has(5)
    assert not ht.has(4)
    assert not ht.has(22)

    # test lookup
    assert ht.lookup(2) == 'hello'
    assert ht.lookup(3) == 'my'
    assert ht.lookup(21) == 'name'
    assert ht.lookup(5) == 'is not Rushi'
    assert ht.lookup(22) == ''

    # test remove
    ht.remove(2)
    ht.remove(3)
    assert ht.to_string() == '4 <21,name>\n5 <5,is not Rushi>\n'
    ht.store(9, "you're")
    ht.store(33, 'welcome')
    assert ht.to_string() == "0 <33,welcome>\n3 <9,you're>\n4 <21,name>\n5 <5,is not Rushi>\n"
    ht.remove(9)
    assert ht.to_string() == '0 <33,welcome>\n4 <21,name>\n5 <5,is not Rushi>\n'
    ht.remove(21)
    assert ht.to_string() == '0 <33,welcome>\n5 <5,is not Rushi>\n'
    ht.remove(33)
    assert ht.to_string() == '5 <5,is not Rushi>\n'
    ht.remove(5)
    assert ht.to_string() == ''
    ht.store(9, "you're")
    assert ht.to_string() == "3 <9,you're>\n"

    # test nuke
    ht.nuke()
    assert ht.to_string() == ''
