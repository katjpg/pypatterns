class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        dp = {0}

        for val in nums:
            dp = dp | {s + val for s in dp}
            if target in dp:
                return True

        return False


"""
time: O(n * target) where target = sum(nums) / 2
- for each of n elements, update up to target sums.

space: O(target)
- dp set holds at most target + 1 distinct sums.

"""
