class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_node = None

        q = 0

        while True:
            if l1 is None and l2 is None:
                if q > 0:
                    list_node = ListNode(val=q, next=list_node)
                    q = 0
                    continue
                else:
                    break

            if l1 is None:
                l1_val = 0
            else:
                l1_val = l1.val

            if l2 is None:
                l2_val = 0
            else:
                l2_val = l2.val

            val = (l1_val + l2_val + q) % 10

            list_node = ListNode(val=val, next=list_node)

            q = (l1_val + l2_val + q) // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return self.reverse_linked_list(list_node)

    def reverse_linked_list(self, list_node: ListNode) -> ListNode:
        previous = None
        current = list_node
        following = list_node

        while current is not None:
            following = list_node.next
            current.next = previous
            previous = current
            current = following

        return previous
