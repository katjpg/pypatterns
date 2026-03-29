class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val

            curr = curr.right


"""
time: O(h + k)
- h to reach the leftmost node, k pops in inorder.
- returns at the kth smallest, skips remaining nodes.

space: O(h) where h = tree height
- stack holds at most h nodes.
- O(log n) for balanced tree, O(n) for skewed tree.

"""
