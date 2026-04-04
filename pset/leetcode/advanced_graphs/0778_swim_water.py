import heapq


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        vis = set()
        heap = [(grid[0][0], 0, 0)]
        vis.add((0, 0))

        while heap:
            t, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in vis:
                    vis.add((nr, nc))
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))

        return -1


"""
time: O(n^2 log n)
- each cell pushed to heap at most once.
- heap ops are O(log n^2) = O(log n).

space: O(n^2)
- vis set and heap each hold at most n^2 entries.

"""
