class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[amount] if dp[amount] <= amount else -1


"""
time: O(amount * n) where n = len(coins)
- fill dp array of size amount + 1
- each entry checks n coins.

space: O(amount)
- dp array of size amount + 1.

"""
