class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, c: int = 0) -> ListNode:
        val = l1.val + l2.val + c

        ret = ListNode(val % 10)

        c = val // 10

        if l1.next or l2.next or c:
            if not l1.next:
                l1.next = ListNode(0)
            if not l2.next:
                l2.next = ListNode(0)

            ret.next = self.addTwoNumbers(l1.next, l2.next, c)

        return ret
