class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")
        self.idx = 0

        def dfs():
            if vals[self.idx] == "N":
                self.idx += 1
                return None

            node = TreeNode(int(vals[self.idx]))
            self.idx += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


# codec = Codec()
# codec.deserialize(codec.serialize(root))


"""
time: O(n) for both serialize and deserialize
- serialize: preorder DFS visits each node once, joins n values.
- deserialize: splits string and reconstructs each node once via self.idx.

space: O(n)
- serialize: res list holds n node values and n+1 "N" entries for null children.
- deserialize: vals array holds the same, recursion depth is O(h).

"""
