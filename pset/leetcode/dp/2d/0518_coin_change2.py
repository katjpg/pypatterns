class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]

        return dp[amount]


"""
time: O(n * amount) where n = len(coins)
- outer loop over coins, inner loop over amounts.

space: O(amount)
- single dp array of size amount + 1.

"""
