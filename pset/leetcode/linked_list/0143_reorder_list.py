class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        first, second = head, prev
        while second:
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first, second = nxt1, nxt2


"""
time: O(n)
- find middle: slow/fast traverse n/2 and n nodes.
- reverse: single pass through second half (n/2 nodes).
- merge: single pass alternating both halves (n/2 nodes).

space: O(1)
- only slow, fast, prev, first, second, nxt, nxt1, nxt2.
- no extra data structures.

"""
