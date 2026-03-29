class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


"""
time: O(n)
- single pass through n nodes.
- each step rewires curr.next -> prev and advances both pointers.

space: O(1)
- only prev, curr, nxt.
- no extra data structures.

"""
