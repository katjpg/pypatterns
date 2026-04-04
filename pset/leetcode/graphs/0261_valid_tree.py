class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        vis = set()

        def dfs(node):
            vis.add(node)
            for nei in graph[node]:
                if nei not in vis:
                    dfs(nei)

        dfs(0)
        return len(vis) == n


"""
time: O(V + E)
- edge count check is O(1).
- DFS visits each node and edge once.

space: O(V + E)
- adjacency list and visited set.

"""
