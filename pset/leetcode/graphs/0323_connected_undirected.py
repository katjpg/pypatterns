class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = list(range(n))

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[rx] = ry
            return True

        cnt = n
        for u, v in edges:
            if union(u, v):
                cnt -= 1
        return cnt


"""
time: O(V + E * a(V))
- a(V) is inverse Ackermann, effectively O(1).
- each edge = a union operation.

space: O(V)
- parent array of size n.

"""
