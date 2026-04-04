class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def sink(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + sink(r + 1, c) + sink(r - 1, c) + sink(r, c + 1) + sink(r, c - 1)

        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    ans = max(ans, sink(r, c))
        return ans


"""
time: O(m * n)
- DFS visits each cell at most once.
- in-place mark to 0 prevents revisits.

space: O(m * n)
- worst case all cells are land in one long path.
- recursion goes m * n deep.

"""
