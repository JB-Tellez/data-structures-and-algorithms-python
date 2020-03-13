from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList,
)
from data_structures_and_algorithms.challenges.ll_merge.ll_merge import merge_lists


def test_merge_nice():
    a = LinkedList([1, 3, 2])
    b = LinkedList([5, 9, 4])

    actual = merge_lists(a, b)
    expected = LinkedList([1, 5, 3, 9, 2, 4])

    assert str(actual) == str(expected)


def test_short_top():
    a = LinkedList([1, 3])
    b = LinkedList([5, 9, 4])

    actual = merge_lists(a, b)
    expected = LinkedList([1, 5, 3, 9, 4])

    assert str(actual) == str(expected)


def test_long_top():
    a = LinkedList([1, 3, 2])
    b = LinkedList([5, 9])

    actual = merge_lists(a, b)
    expected = LinkedList([1, 5, 3, 9, 2])

    assert str(actual) == str(expected)
