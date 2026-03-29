class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Node | None") -> "Node | None":
        if not head:
            return None

        hashmap = {}

        curr = head
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = hashmap[curr]
            if curr.next:
                copy.next = hashmap[curr.next]
            if curr.random:
                copy.random = hashmap[curr.random]
            curr = curr.next

        return hashmap[head]


"""
time: O(n)
- first pass: creates n copy nodes and stores each in hashmap.
- second pass: links .next and .random via O(1) hashmap lookups.

space: O(n)
- hashmap maps n original nodes to n copy nodes.
- deep copy creates n new nodes.

"""
