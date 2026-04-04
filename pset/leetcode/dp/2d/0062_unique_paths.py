class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                row[j] += row[j - 1]
        return row[-1]


"""
time: O(m * n)
- fill each of (m-1) rows, each with n-1.

space: O(n)
- single row reused across all iterations.

"""
