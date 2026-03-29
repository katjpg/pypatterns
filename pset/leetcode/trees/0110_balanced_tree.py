class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left == -1 or right == -1 or abs(left - right) >= 2:
                return -1

            return max(left, right) + 1

        return dfs(root) != -1


"""
time: O(n)
- DFS visits each node once, computing subtree height.
- returns -1 flag if any subtree is unbalanced or height difference >= 2.

space: O(h) where h = tree height
- recursion depth equals h.
- O(log n) for balanced tree, O(n) for skewed tree.

"""
