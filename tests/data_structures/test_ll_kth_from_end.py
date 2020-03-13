import pytest

from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList,
    TargetError,
)

# head -> [1] -> [3] -> [8] -> [2] -> X	0	2
# head -> [1] -> [3] -> [8] -> [2] -> X	2	3
# head -> [1] -> [3] -> [8] -> [2] -> X	6	Exception


def test_zero_from_end():
    ll = LinkedList()
    ll.append("apples")
    actual = ll.kth_from_end(0)
    expected = "apples"
    assert actual == expected


def test_empty_out_of_range():
    ll = LinkedList()

    with pytest.raises(IndexError):
        ll.kth_from_end(0)


def test_3_from_end():
    ll = LinkedList([1, 7, 19, 8, 2])
    actual = ll.kth_from_end(3)
    expected = 7
    assert actual == expected


def test_out_of_range():
    ll = LinkedList([1, 3, 8, 2])

    with pytest.raises(IndexError):
        ll.kth_from_end(6)
