def reverse(list_node):
    previous = None
    current = list_node
    following = list_node

    while current is not None:
        following = list_node.next
        current.next = previous
        previous = current
        current = following

    return previous
