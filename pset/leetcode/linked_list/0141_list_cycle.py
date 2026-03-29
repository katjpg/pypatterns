class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


"""
time: O(n)
- slow advances 1 step, fast advances 2 steps per iteration.
- if a cycle exists, slow and fast converge within at most n iterations.

space: O(1)
- only slow, fast.
- no extra data structures.

"""
