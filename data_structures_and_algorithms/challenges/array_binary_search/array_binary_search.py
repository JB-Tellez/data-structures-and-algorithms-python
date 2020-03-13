def binary_search(lst, target, left=0, right=None):

    if right == None:
        right = len(lst) - 1

    # base case 1
    if right < left:
        return -1

    mid = (right - left) // 2 + left

    candidate = lst[mid]

    # base case 2
    if target == candidate:
        return mid

    if target < candidate:
        # go smaller by decreasing right index
        right = mid - 1
    else:
        # go bigger by increasing right index
        left = mid + 1

    # recurse
    return binary_search(lst, target, left, right)
