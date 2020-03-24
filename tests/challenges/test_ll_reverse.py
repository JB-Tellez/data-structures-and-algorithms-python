# from reverse_linked_list import reverse_linked_list, LinkedList
from data_structures_and_algorithms.challenges.ll_reverse.ll_reverse import (
    reverse_linked_list,
)
from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList,
)


def test_reverse_none():
    ll = LinkedList()
    expected = ""
    flipped = reverse_linked_list(ll)
    actual = str(flipped)
    assert actual == expected


def test_reverse_one():
    ll = LinkedList(["apple"])
    expected = "[apple],"
    flipped = reverse_linked_list(ll)
    actual = str(flipped)
    assert actual == expected


def test_reverse_three():
    ll = LinkedList(["apple", "banana", "cucumber"])
    expected = "[cucumber],[banana],[apple],"
    flipped = reverse_linked_list(ll)
    actual = str(flipped)
    assert actual == expected
