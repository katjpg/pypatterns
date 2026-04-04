class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = sum(nums)
        if (total + target) % 2 or abs(target) > total:
            return 0

        pos = (total + target) // 2
        dp = [0] * (pos + 1)
        dp[0] = 1

        for val in nums:
            for j in range(pos, val - 1, -1):
                dp[j] += dp[j - val]

        return dp[pos]


"""
time: O(n * pos) where pos = (sum + target) / 2
- n elements, each updates pos entries.

space: O(pos)
- single dp array.

"""
