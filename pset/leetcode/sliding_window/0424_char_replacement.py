class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxFreq = 0
        left = 0
        maxLen = 0

        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right], 0)
            maxFreq = max(maxFreq, freq[s[right]])

            # chars to replace > k, shrink by moving left
            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen


"""
time: O(n)
- right pointer visits each character once.
- left pointer only moves forward, total moves <= n.

space: O(1)
- freq hashmap holds at most 26 uppercase letters.
- only maxFreq, left, right, maxLen.

"""
