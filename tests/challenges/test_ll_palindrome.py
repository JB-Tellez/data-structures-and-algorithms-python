from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList,
)
from data_structures_and_algorithms.challenges.ll_palindrome.ll_palindrome import (
    is_palindrome,
)


def test_mom():
    lst = LinkedList("mom")
    actual = is_palindrome(lst)
    expected = True
    assert actual == expected


def test_peep():
    lst = LinkedList("peep")
    actual = is_palindrome(lst)
    expected = True
    assert actual == expected
