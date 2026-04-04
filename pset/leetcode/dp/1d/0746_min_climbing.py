class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        a, b = 0, 0
        for i in range(2, len(cost) + 1):
            a, b = b, min(b + cost[i - 1], a + cost[i - 2])
        return b


"""
time: O(n)
- single pass from step 2 -> step n.

space: O(1)
- two variables track min cost to reach previous two steps.

"""
