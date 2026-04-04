class Solution:
    def rob(self, nums: list[int]) -> int:
        a, b = 0, 0
        for val in nums:
            a, b = b, max(b, a + val)
        return b


"""
time: O(n)
- single pass over all houses.

space: O(1)
- a = best up to two houses back, b = best up to previous house.

"""
