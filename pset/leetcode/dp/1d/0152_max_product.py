class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1

        for val in nums:
            candidates = (val, curMax * val, curMin * val)
            curMax = max(candidates)
            curMin = min(candidates)
            res = max(res, curMax)

        return res


"""
time: O(n)
- one pass over n elements.
- each computes max/min from 3 candidates.

space: O(1)
- three variables: curMax, curMin, res.

"""
