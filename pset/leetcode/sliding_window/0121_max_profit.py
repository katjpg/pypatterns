class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                profit = price - minPrice
                maxProfit = max(maxProfit, profit)

        return maxProfit


"""
time: O(n)
- single pass through prices array.
- minPrice and maxProfit updated in constant time per step.

space: O(1)
- only minPrice, maxProfit, profit.
- no extra data structures.

"""
