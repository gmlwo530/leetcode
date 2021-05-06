class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list = []
        l2_list = []
        s = 0

        while True:
            if l1 is not None:
                l1_list.append(l1.val)
                l1 = l1.next

            if l2 is not None:
                l2_list.append(l2.val)
                l2 = l2.next

            if l1 is None and l2 is None:
                break

        for idx, ele in enumerate(l1_list):
            s += ele * (10 ** idx)

        for idx, ele in enumerate(l2_list):
            s += ele * (10 ** idx)

        if s == 0:
            return ListNode(val=0, next=None)

        len_s = 0
        list_node = None

        while True:
            if s // (10 ** len_s) < 1:
                break
            len_s += 1

        for i in reversed(range(len_s)):
            if 10 ** i > s:
                val = 0
            else:
                val = s // (10 ** i)

            list_node = ListNode(val=val, next=list_node)

            s -= val * (10 ** i)

        return list_node
