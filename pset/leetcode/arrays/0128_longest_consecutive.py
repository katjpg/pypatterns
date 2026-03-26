class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hashset = set(nums)
        max_length = 0

        for n in hashset:
            if (n - 1) not in hashset:
                length = 1
                while (n + length) in hashset:
                    length += 1
                max_length = max(max_length, length)
        return max_length


""" 
time: O(n)
- set() lookups are O(1) on average.
- start count from start of sequence.

space: O(n)
- set() stores all unique nums from input.

"""
