class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.mergeTwo(l1, l2))
            lists = merged

        return lists[0]

    def mergeTwo(self, l1, l2):
        temp = ListNode()
        tail = temp

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2

        return temp.next


"""
time: O(n log k)
- log k iterations of pairwise merging, each processing all n nodes.
- each mergeTwo call is O(n1 + n2).

space: O(k)
- merged array holds at most k/2 list heads per iteration.
- mergeTwo uses only temp, tail.

"""
