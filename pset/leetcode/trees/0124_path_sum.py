class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.res = root.val

        def dfs(node):
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            self.res = max(self.res, node.val + left + right)

            return node.val + max(left, right)

        dfs(root)
        return self.res


"""
time: O(n)
- DFS visits each node exactly once.
- O(1) max comparison and path sum update per node.

space: O(h) where h = tree height
- recursion depth equals h.
- O(log n) for balanced tree, O(n) for skewed tree.

"""
