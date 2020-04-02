from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList,
)

from data_structures_and_algorithms.challenges.ll_reverse.ll_reverse import (
    reverse_linked_list,
)


def is_palindrome(lst):
    current = lst.head
    items = []
    while current:
        items.append(current.value)
        current = current.next

    mid = len(items) // 2

    for i in range(mid + 1):
        if items[i] != items[-1 - i]:
            return False

    return True


def is_palindrome_impure(lst):

    forward = str(lst)

    backward = str(reverse_linked_list(lst))

    return forward == backward
