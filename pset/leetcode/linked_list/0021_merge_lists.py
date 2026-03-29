class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        temp = ListNode()
        tail = temp

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2

        return temp.next


"""
time: O(n + m)
- single pass comparing heads of list1 and list2.
- each node appended to tail exactly once.

space: O(1)
- only temp, tail.
- no extra data structures.

"""
