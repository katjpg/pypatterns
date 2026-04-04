import heapq


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        vis = set()
        heap = [(0, 0)]
        ans = 0

        while len(vis) < n:
            cost, u = heapq.heappop(heap)
            if u in vis:
                continue
            vis.add(u)
            ans += cost
            for v in range(n):
                if v not in vis:
                    dist = abs(points[u][0] - points[v][0]) + abs(
                        points[u][1] - points[v][1]
                    )
                    heapq.heappush(heap, (dist, v))

        return ans


"""
time: O(n^2 log n)
- complete graph with n^2 edges.
- each edge pushed to heap at most once.
- heap ops are O(log n^2) = O(log n).

space: O(n^2)
- heap can hold up to n^2 entries in worst case.

"""
