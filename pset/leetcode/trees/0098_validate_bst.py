class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def valid(node, low, high):
            if not node:
                return True

            if low is not None and node.val <= low:
                return False
            if high is not None and node.val >= high:
                return False

            return valid(node.left, low, node.val) and valid(node.right, node.val, high)

        return valid(root, None, None)


"""
time: O(n)
- DFS visits each node exactly once.
- O(1) range check per node using low and high bounds.

space: O(h) where h = tree height
- recursion depth equals h.
- O(log n) for balanced tree, O(n) for skewed tree.

"""
