class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


"""
time: O(log n)
- search interval 1/2 each iteration.
- compare mid to right to determine which half contains min.

space: O(1)
- only left, right, mid.
- no extra data structures.

"""
