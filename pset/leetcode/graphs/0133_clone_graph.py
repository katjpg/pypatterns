class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        if not node:
            return None

        clones = {}

        def dfs(cur):
            if cur in clones:
                return clones[cur]
            clone = Node(cur.val)
            clones[cur] = clone
            for nei in cur.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone

        return dfs(node)


"""
time: O(V + E)
- DFS visits each node once and traverses each edge once.

space: O(V)
- clones dict holds one entry per node.
- recursion depth at most V.

"""
