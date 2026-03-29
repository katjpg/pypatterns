class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False


"""
time: O(m * n)
- DFS traverses each of m nodes in root.
- at each node, isSameTree compares up to n nodes in subRoot.

space: O(h) where h = height of root
- recursion depth equals h for isSubtree traversal.
- isSameTree adds at most O(h_sub) on top, where h_sub = height of subRoot.

"""
