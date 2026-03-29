class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next

        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head.next = self.reverseKGroup(curr, k)

        return prev


"""
time: O(n)
- n/k recursive calls, each checking and reversing k nodes.
- each node visited at most twice (check + reverse).

space: O(n/k)
- recursion depth is n/k, one frame per k-group.
- each call stores only prev, curr, nxt.

"""
