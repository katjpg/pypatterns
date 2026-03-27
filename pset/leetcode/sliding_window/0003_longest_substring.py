class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, maxLen = 0, 0
        seen = {}

        for i, ch in enumerate(s):
            if ch in seen and seen[ch] >= start:
                start = seen[ch] + 1
            maxLen = max(maxLen, i - start + 1)
            seen[ch] = i

        return maxLen

"""
time: O(n)
- single pass with sliding window, each char visited once.
- hashmap lookup and update are O(1) per step.

space: O(k)
- seen hashmap stores at most k unique characters.
- k <= min(n, size of char set).

"""
