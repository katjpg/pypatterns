class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return

            if depth == len(res):
                res.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res


"""
time: O(n)
- DFS visits each node exactly once.
- right subtree traversed before left at each node.

space: O(h) where h = tree height
- recursion depth equals h.
- O(log n) for balanced tree, O(n) for skewed tree.

"""
