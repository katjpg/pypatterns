class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False


"""
time: O(n)
- DFS visits each node once, comparing values at each position.
- `and` skips right subtree comparison if left subtrees differ.

space: O(h) where h = tree height
- recursion depth equals h.
- O(log n) for balanced tree, O(n) for skewed tree.

"""
