import pytest
from challenges.left_join.left_join import left_join
from data_structures.hashtable.hashtable import Hashtable


def test_left_join_simple(ht_left, ht_right):
    actual = left_join(ht_left, ht_right)
    expected = [
        ["outfit", "garb", None],
        ["guide", "usher", "follow"],
        ["wrath", "anger", "delight"],
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
    ]

    assert actual == expected


def test_left_join_only_left(ht_left):
    actual = left_join(ht_left, Hashtable())
    expected = [
        ["outfit", "garb", None],
        ["guide", "usher", None],
        ["wrath", "anger", None],
        ["diligent", "employed", None],
        ["fond", "enamored", None],
    ]
    assert actual == expected


def test_left_join_only_right(ht_right):
    actual = left_join(Hashtable(), ht_right)
    expected = []
    assert actual == expected


def test_left_join_both_empty():
    actual = left_join(Hashtable(), Hashtable())
    expected = []
    assert actual == expected


@pytest.fixture
def ht_left():
    ht = Hashtable()
    ht.add("fond", "enamored")
    ht.add("wrath", "anger")
    ht.add("diligent", "employed")
    ht.add("outfit", "garb")
    ht.add("guide", "usher")
    return ht


@pytest.fixture
def ht_right():
    ht = Hashtable()
    ht.add("fond", "averse")
    ht.add("wrath", "delight")
    ht.add("diligent", "idle")
    ht.add("guide", "follow")
    ht.add("flow", "jam")
    return ht