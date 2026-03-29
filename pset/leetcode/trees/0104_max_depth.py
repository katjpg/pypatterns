class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


"""
time: O(n)
- DFS visits each node exactly once.
- O(1) comparison of left and right subtree depths per node.

space: O(h) where h = tree height
- recursion depth equals h.
- O(log n) for balanced tree, O(n) for skewed tree.

"""
