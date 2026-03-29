class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


"""
time: O(log n)
- search interval 1/2 each iteration.
- at most log2(n) comparisons.

space: O(1)
- only left, right, mid.
- no extra data structures.

"""
