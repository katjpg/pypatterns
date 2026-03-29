class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        temp = ListNode(0, head)
        slow, fast = temp, head

        for _ in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return temp.next


"""
time: O(n)
- fast advances n steps, then both pointers traverse remaining nodes.
- single pass through list.

space: O(1)
- only temp, slow, fast.
- no extra data structures.

"""
