from collections import deque


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            vis = set(starts)
            queue = deque(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in vis
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        vis.add((nr, nc))
                        queue.append((nr, nc))
            return vis

        pac = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
        atl = [(r, cols - 1) for r in range(rows)] + [
            (rows - 1, c) for c in range(cols)
        ]

        return [list(c) for c in bfs(pac) & bfs(atl)]


"""
time: O(m * n)
- two BFS passes, each visits every cell at most once.

space: O(m * n)
- pac and atl sets each hold at most m * n entries.
- BFS avoids recursion depth issues on large grids.

"""
