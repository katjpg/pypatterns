class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
        return [-1, 1]


""" 
time: O(n)
- iterate through array once.
- hashmap lookup/insert is O(1) on average

space: O(n)
- hashmap stores n elements

"""
