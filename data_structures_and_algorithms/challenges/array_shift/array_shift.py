def array_shift(lst, item):
    """insert item into middle of list

    Arguments:
        lst {list} -- original list
        item {any} -- the item to insert

    Returns:
        list -- new list with items shifted over to make room for insertion to middle
    """
    mid = (len(lst) + 1) // 2

    left = lst[:mid]
    right = lst[mid:]

    return left + [item] + right
