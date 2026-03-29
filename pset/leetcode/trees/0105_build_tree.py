class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        hashmap = {val: i for i, val in enumerate(inorder)}
        self.idx = 0

        def dfs(left, right):
            if left > right:
                return None

            val = preorder[self.idx]
            self.idx += 1
            mid = hashmap[val]

            node = TreeNode(val)
            node.left = dfs(left, mid - 1)
            node.right = dfs(mid + 1, right)

            return node

        return dfs(0, len(inorder) - 1)


"""
time: O(n)
- each node constructed exactly once.
- hashmap gives O(1) inorder index lookup per node.

space: O(n)
- hashmap stores n value-index pairs.
- recursion depth is O(h), output tree is n nodes.

"""
