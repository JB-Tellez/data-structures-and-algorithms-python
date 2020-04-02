def reverse_linked_list(ll):
    prev = None
    current = ll.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    ll.head = prev

    return ll
