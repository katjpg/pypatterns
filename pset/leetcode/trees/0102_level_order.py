class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            level = []
            nextQueue = []
            for node in queue:
                level.append(node.val)
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            res.append(level)
            queue = nextQueue

        return res


"""
time: O(n)
- BFS visits each node exactly once.
- each node appended to level and its children to nextQueue in O(1).

space: O(w) where w = max width of tree
- queue holds at most one level of nodes at a time.
- largest level in a balanced tree has up to n/2 nodes.

"""
