class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_list_node = None
        prev_list_node = None

        carry = 0

        while True:
            if l1 is None and l2 is None:
                if carry > 0:
                    prev_list_node.next = ListNode(val=carry)
                    carry = 0
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

            val = (l1_val + l2_val + carry) % 10

            if prev_list_node:
                next_list_node = ListNode(val=val)
                prev_list_node.next = next_list_node
                prev_list_node = next_list_node
            else:
                result_list_node = ListNode(val=val)
                prev_list_node = result_list_node

            carry = (l1_val + l2_val + carry) // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result_list_node
