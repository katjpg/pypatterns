class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robLinear(arr):
            a, b = 0, 0
            for val in arr:
                a, b = b, max(b, a + val)
            return b

        return max(robLinear(nums[1:]), robLinear(nums[:-1]))


"""
time: O(n)
- two linear passes over n-1 elements each.

space: O(1)
- two variables per pass, no DP array.
- slicing (`nums[1:]`, `nums[:-1]`) creates O(n) copies.

"""
