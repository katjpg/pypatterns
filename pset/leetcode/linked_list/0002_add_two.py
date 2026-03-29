class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        temp = ListNode()
        res = temp
        total = carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            carry = total // 10
            temp.next = ListNode(total % 10)
            temp = temp.next

        return res.next


"""
time: O(max(m, n))
- single pass through both lists, processing one digit per iteration.
- loop continues until both lists are traversed and carry = 0.

space: O(max(m, n))
- result list has at most max(m, n) + 1 nodes (extra node if final carry).
- only temp, res, carry, total.

"""
