class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        vals = [1] + nums + [1]
        n = len(vals)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                for k in range(left + 1, right):
                    coins = vals[left] * vals[k] * vals[right]
                    dp[left][right] = max(
                        dp[left][right], dp[left][k] + coins + dp[k][right]
                    )

        return dp[0][n - 1]


"""
time: O(n^3)
- three nested loops: subproblem length, left boundary, last balloon to burst.

space: O(n^2)
- dp table of size n x n.

"""
