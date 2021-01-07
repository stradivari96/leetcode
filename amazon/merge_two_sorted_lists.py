def mergeTwoLists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.val < l2.val:
        result = l1
        l1 = l1.next
    else:
        result = l2
        l2 = l2.next

    node = result
    while l1 and l2:
        if l1.val < l2.val:
            node.next = l1
            l1 = l1.next
            node = node.next
        else:
            node.next = l2
            l2 = l2.next
            node = node.next

    if l1:
        node.next = l1
    if l2:
        node.next = l2

    return result
