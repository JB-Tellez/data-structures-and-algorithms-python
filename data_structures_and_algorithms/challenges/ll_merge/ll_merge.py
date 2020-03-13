def merge_lists(a, b):

    current_a = a.head
    current_b = b.head

    while current_a and current_b:
        next_a = current_a.next
        next_b = current_b.next

        current_a.next = current_b

        if not next_a:
            break

        current_b.next = next_a

        current_a = next_a
        current_b = next_b

    return a
