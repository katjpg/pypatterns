class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        ans = 0
        stack = [(root, root.val)]

        while stack:
            node, maxVal = stack.pop()

            if node.val >= maxVal:
                ans += 1
                maxVal = node.val

            if node.left:
                stack.append((node.left, maxVal))
            if node.right:
                stack.append((node.right, maxVal))

        return ans


"""
time: O(n)
- iterative DFS visits each node exactly once.
- O(1) comparison of node.val against maxVal per node.

space: O(h) where h = tree height
- stack holds at most h (node, maxVal) pairs.
- O(log n) for balanced tree, O(n) for skewed tree.

"""
