class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        hold, sold, cool = float("-inf"), 0, 0

        for p in prices:
            prevHold = hold
            hold = max(hold, cool - p)
            cool = max(cool, sold)
            sold = prevHold + p

        return max(sold, cool)


"""
time: O(n)
- one pass, three state updates per day.

space: O(1)
- three variables: hold, sold, cool.

"""
